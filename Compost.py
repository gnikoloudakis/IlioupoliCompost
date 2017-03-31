import logging
from datetime import datetime, timedelta

from flask import Flask, render_template, request, redirect, json, session
from flask_mongoengine import MongoEngine
from flask_security import Security, MongoEngineUserDatastore, UserMixin, RoleMixin, login_required, roles_required
from ext import myFlags

# from logging.handlers import RotatingFileHandler

app = Flask(__name__)
app.config.from_object('config')
db = MongoEngine(app)

logging.basicConfig()


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document, UserMixin):
    password = db.StringField(max_length=512)
    email = db.StringField(max_length=255, unique=True)
    active = db.BooleanField(default=True)
    date_created = db.DateTimeField(default=datetime.now(), format='%d-%m-%Y')
    confirmed_at = db.DateTimeField(format='%d-%m-%Y')
    last_login_at = db.DateTimeField(format='%d-%m-%Y')
    current_login_at = db.DateTimeField(format='%d-%m-%Y')
    last_login_ip = db.StringField(max_length=45)
    current_login_ip = db.StringField(max_length=45)
    login_count = db.IntField()
    roles = db.ListField(db.ReferenceField(Role))


user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def hello_world():
    return redirect('/login')


@app.route('/dashboard')
#@login_required
def dashboard():
    return render_template('Dashboard.html')


@app.route('/charts')
#@login_required
def charts():
    return render_template('Charts.html')


@app.route('/settings')
#@login_required
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
#@login_required
def Setttings_saveall():
    from modules.DatabaseFunctions import saveSettings
    success = saveSettings(request.form)
    if success:
        app.logger.debug("Saved settings")
    else:
        app.logger.error("Could not save settings")
    return redirect('/settings')


@app.route('/controls')
#@login_required
def controls():
    return render_template('Controls.html')


@app.route('/log')
#@login_required
def Logs():
    from models.models import Log
    log = Log.objects
    return render_template('Logs.html', log=log)


#@login_required
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
#@login_required
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


@app.route('/api/measurements/add', methods=['POST', 'GET'])
def add_measurements():
    print ("add meas debug")
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


@app.route('/api/measurements/get/last/<m_type>', methods=["GET"])
def get_last_measurement(m_type):
    m = [{}]
    from modules.MeasurementsFunctions import getLast
    success, measurements = getLast(m_type)
    if success:
        m = json.loads(measurements)
    else:
        print ("ould NOT get last measurement")
    return json.dumps(m)
    # if success:
    #     print json.loads(measurements)
    #     m = json.dumps(measurements)
    # else:
    #     return 'Did NOT get Measurements'
    # return m


@app.route('/api/flags/get', methods=['GET'])
def getFlags():
    f = {'Motor1': myFlags.Motor1, 'Motor2': myFlags.Motor2, 'Vent': myFlags.Vent, 'Fan': myFlags.Fan, 'Door': myFlags.Door}
    # print (f)
    return json.dumps(f)


@app.route('/api/motors/m1l', methods=['GET'])
def m1l():
    from modules.MotorFunctions import Motor_1_Left
    if Motor_1_Left():
        print ("Motor 1 started LEFT")
    else:
        print ("Could NOT start Motor 1 LEFT")
    return 'Motor 1 LEFT'


@app.route('/api/motors/m1r', methods=['GET'])
def m1r():
    from modules.MotorFunctions import Motor_1_Right
    if Motor_1_Right():
        print ("Motor 1 started RIGHT")
    else:
        print ("Could NOT start Motor 1 RIGHT")
    return 'Motor 1 RIGHT'


@app.route('/api/motors/m1stop', methods=['GET'])
def m1stop():
    from modules.MotorFunctions import Motor_1_Stop
    if Motor_1_Stop():
        print ("Motor 1 Stopped")
    else:
        print ("Could NOT stop Motor 1")
    return 'Motor 1 STOP'


@app.route('/api/motors/m2l', methods=['GET'])
def m2l():
    from modules.MotorFunctions import Motor_2_Left
    if Motor_2_Left():
        print ("Motor 2 started LEFT")
    else:
        print ("Could NOT start Motor 2 LEFT")
    return 'Motor 2 LEFT'


@app.route('/api/motors/m2r', methods=['GET'])
def m2r():
    from modules.MotorFunctions import Motor_2_Right
    if Motor_2_Right():
        print ("Motor 2 started RIGHT")
    else:
        print ("Could NOT start Motor 2 RIGHT")
    return 'Motor 2 RIGHT'


@app.route('/api/motors/m2stop', methods=['GET'])
def m2stop():
    from modules.MotorFunctions import Motor_2_Stop
    if Motor_2_Stop():
        print ("Motor 2 Stopped")
    else:
        print ("Could NOT stop Motor 2")
    return 'Motor 2 STOP'


@app.route('/api/motors/fan', methods=['GET'])
def fan():
    from modules.MotorFunctions import StartFan
    if StartFan():
        print ("Fan Started")
    else:
        print ("Could NOT Start Fan")
    return 'Fan START'


@app.route('/api/motors/stopfan', methods=['GET'])
def stopfan():
    from modules.MotorFunctions import StopFan
    if StopFan():
        print ("Fan Stopped")
    else:
        print ("Could NOT Stop Fan")
    return 'Fan STOP'


@app.route('/api/motors/vent', methods=['GET'])
def vent():
    from modules.MotorFunctions import StartVent
    if StartVent():
        print ("Vent Started")
    else:
        print ("Could NOT Start Vent")
    return 'Vent START'


@app.route('/api/motors/stopvent', methods=['GET'])
def stopvent():
    from modules.MotorFunctions import StopVent
    if StopVent():
        print ("Vent Stopped")
    else:
        print ("Could NOT Stop Vent")
    return 'Vent STOP'


if __name__ == '__main__':
    from modules.SetupSchedulers import init_sched
    from modules.initDB import initDb

    # readVariables()
    init_sched()
    # initDB()
    # socketio.run(app=app, host='0.0.0.0', port=5000, debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)
