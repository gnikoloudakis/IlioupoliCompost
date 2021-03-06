import datetime
import json
import os
import random

import requests
from apscheduler.schedulers.background import BackgroundScheduler

from modules.RoutineFunctions import *
from modules.SetupFlags import readFlags

# The "apscheduler." prefix is hard coded
# blockingScheduler = BlockingScheduler()
scheduler2 = BackgroundScheduler()
# scheduler3 = BackgroundScheduler()

scheduler = BackgroundScheduler({
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///' + app.root_path + os.sep + 'example1.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '2'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '2'
    },
    'apscheduler.job_defaults.coalesce': 'True',
    # 'apscheduler.job_defaults.misfire_grace_time': 5,
    'apscheduler.job_defaults.max_instances': '2',
    'apscheduler.timezone': 'Europe/Athens',
})


# def initmeas():
# url1 = sys.argv[1] if len(sys.argv) > 1 else 'sqlite:///' + app.root_path + os.sep + 'example1.sqlite'
# scheduler.add_jobstore('sqlalchemy', url=url1)


def add_measurements():
    m_type = ["soil_temp", "soil_hum", "air_temp", "air_hum", "outside_temp", "outside_hum", "outside_light"]
    meas = {"m_type": m_type[random.randint(0, 6)],
            "m_value": random.uniform(20.0, 80.5)}
    requests.post("http://localhost:5000/api/measurements/add", data=json.dumps(meas))
    app.logger.debug(str(meas) + ' posted measurements ' + str(datetime.datetime.now()))


###########################################################################################################################################

def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The job worked :)')


# scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
# blockingScheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
###########################################################################################################################################
def systemrestart():
    os.system("sudo reboot")


###########################################################################################################################################
def GetVariables():
    requests.get('http://localhost:5000/api/variables/read')


def init_sched():
    scheduler.add_job(pushSoilBack, 'cron', day_of_week='mon-fri', hour=datetime.datetime.strptime(Settings.objects.first().daily_soil_backward_time, '%H:%M%p').hour, jobstore='default', executor='default', replace_existing=True, id='soilBack')
    scheduler.add_job(soilHomogenization, 'cron', day_of_week='mon-fri', hour=datetime.datetime.strptime(Settings.objects.first().daily_steering_time, '%H:%M%p').hour, jobstore='default', executor='default', replace_existing=True, id='soilHomogenization')
###########    # scheduler.add_job(systemrestart, 'cron', day_of_week='mon-fri', hour=24, jobstore='default', executor='default', replace_existing=True, id='sysRestart')

###########    # scheduler2.add_job(add_measurements, 'interval', minutes=1)#, jobstore='default', executor='default', replace_existing=True, id='add_meas')
    scheduler.add_job(hourlyVentilation, 'interval', hours=1, jobstore='default', executor='default', replace_existing=True, id='vent', coalesce=True)
    scheduler2.add_job(readFlags, 'interval', seconds=5, replace_existing=True, id='readFlags', coalesce=True)  # , jobstore='default', executor='default'
###########    # scheduler3.add_job(readVariables, 'interval', seconds=5, replace_existing=True, id='readVariables', coalesce=True, max_instances=10)
    scheduler2.add_job(GetVariables, 'interval', minutes=5, replace_existing=True, id='readVariables', coalesce=True, misfire_grace_time=5, max_instances=10)  # , jobstore='default', executor='default'

    scheduler.start()
    scheduler2.start()
    # scheduler3.start()

################################################################################################################################################
