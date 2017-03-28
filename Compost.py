import logging
from flask_socketio import SocketIO, emit
from flask import Flask, render_template, request, redirect
from flask_mongoengine import MongoEngine

# from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

socketio = SocketIO(app)

logging.basicConfig()

# Globals
Motor1 = False
Motor2 = False
Fan = False
Vent = False
Door = False


# logHandler = RotatingFileHandler(app.root_path + os.sep + 'info.log', maxBytes=1000, backupCount=1)
# # set the log handler level
# logHandler.setLevel(logging.DEBUG)
# logHandler.setLevel(logging.ERROR)
#
# # set the app logger level
# # app.logger.setLevel(logging.DEBUG)
#
# app.logger.addHandler(logHandler)


@app.route('/')
def hello_world():
    return render_template('base/Base.html')


@app.route('/dashboard')
def dashboard():
    return render_template('Dashboard.html')


@app.route('/charts')
def charts():
    return render_template('Charts.html')


@app.route('/settings')
def settings():
    from modules.DatabaseFunctions import getSettings
    context = []
    success, settings = getSettings()
    if success:
        context = settings
    else:
        app.logger.error("failed to get settings")
    return render_template('Settings.html', context=context)


@app.route('/settings/saveall', methods=['POST'])
def Setttings_saveall():
    from modules.DatabaseFunctions import saveSettings
    success = saveSettings(request.form)
    if success:
        app.logger.debug("Saved settings")
    else:
        app.logger.error("Could not save settings")
    return redirect('/settings')


@app.route('/controls')
def controls():
    return render_template('Controls.html')


@app.route('/log')
def Logs():
    from models.models import Log
    log = Log.objects
    return render_template('Logs.html', log=log)


@app.route('/log/clear')
def clearLog():
    from modules.DatabaseFunctions import dropLog
    success = dropLog()
    if success:
        app.logger.debug("Dropped Log file")
    else:
        app.logger.error("Could not drop Log file")
    return redirect('/log')


@app.route('/errors')
def Errors():
    from models.models import Errors
    errors = Errors.objects
    return render_template('Errors.html', errors=errors)


@app.route('/errors/clear')
def clearErrors():
    from modules.DatabaseFunctions import dropErrors
    success = dropErrors()
    if success:
        app.logger.debug("Dropped Error file")
    else:
        app.logger.error("Could not drop Error file")
    return redirect('/errors')


@app.route('/api/db/init', methods=["GET"])
def initDB():
    from modules.initDB import initDb
    success = initDb()
    if success:
        return "Settings Initialized"
    else:
        return "Did NOT initialize settings"


@app.route('/api/devices/add', methods=['POST'])
def add_device():
    from modules.DevicesFunctions import add
    success = add(request.data)
    if success:
        return 'added device'
    else:
        return 'Did NOT add device'


@app.route('/api/devices/update', methods=['POST'])
def update_device():
    from modules.DevicesFunctions import update
    success = update(request.data)
    if success:
        return 'Updated Device'
    else:
        return 'Did NOT Update device'


@app.route('/api/measurements/add', methods=['POST'])
def add_measurements():
    from modules.MeasurementsFunctions import add
    success = add(request.data)
    if success:
        return 'Added Measurement'
    else:
        return 'Dit NOT Add measurement'


@app.route('/api/measurements/delete', methods=['GET'])
def drop_measurements():
    from modules.MeasurementsFunctions import drop
    success = drop()
    if success:
        return 'Dropped Measurements'
    else:
        return 'Did NOT drop measurements'


@app.route('/api/measurements/get/<m_type>', methods=["GET"])
def get_measurements(m_type):
    from modules.MeasurementsFunctions import get
    success, measurements = get(m_type)
    if success:
        return measurements
    else:
        return 'Did NOT get Measurements'


@socketio.on('flags')
def socketTest(data):
    print (data)


if __name__ == '__main__':
    from modules.SetupSchedulers import init_sched
    from modules.VariablesFunctions import readVariables

    readVariables()
    init_sched()
    socketio.run(app=app, host='0.0.0.0', port=5000)
