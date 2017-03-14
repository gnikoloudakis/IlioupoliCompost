import sys
import os
from apscheduler.schedulers.background import BackgroundScheduler
from Compost import app
from tzlocal import get_localzone
import random
import requests
import json
import datetime


# The "apscheduler." prefix is hard coded
scheduler = BackgroundScheduler({
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///' + app.root_path + os.sep + 'example1.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '1'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '1',
    'apscheduler.timezone': 'Europe/Athens',
})


# def initmeas():
# url1 = sys.argv[1] if len(sys.argv) > 1 else 'sqlite:///' + app.root_path + os.sep + 'example1.sqlite'
# scheduler.add_jobstore('sqlalchemy', url=url1)


def add_measurements():
    m_type = ["soil_temp", "soil_hum", "air_temp", "air_hum", "outside_temp", "outside_hum", "outside_light"]
    meas = {"m_type": m_type[random.randint(0, 6)],
            "m_value": random.uniform(20.0, 80.5)}
    requests.post("http://127.0.0.1:5000/api/measurements/add", data=json.dumps(meas))
    app.logger.debug(str(meas) + ' posted measurements ' + str(datetime.datetime.now()))


def init_sched():
    scheduler.add_job(add_measurements, 'interval', minutes=1, jobstore='default', executor='default', replace_existing=True, id='task')
    scheduler.start()
