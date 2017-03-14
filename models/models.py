import datetime

from Compost import db


# ##################    MODELS     ###################################
class Devices(db.Document):
    name = db.StringField(unique=True, max_length=50)
    ip = db.StringField(unique=True, max_length=50)


class Settings(db.Document):
    daily_soil_backward_time = db.StringField(default='14:00pm')
    daily_steering_time = db.StringField(default='06:00am')
    steering_duration = db.StringField(max_length=10, default='30000')
    motor_F_duration = db.StringField(max_length=10, default=60)
    motor_B_duration = db.StringField(max_length=10, default=60)
    motor_R_duration = db.StringField(max_length=10, default=60)
    motor_L_duration = db.StringField(max_length=10, default=60)
    vent_duration = db.StringField(max_length=10, default=300)
    lowest_soil_humidity = db.StringField(max_length=10, default='55')
    highest_soil_humidity = db.StringField(max_length=10, default='65')
    lowest_soil_temperature = db.StringField(max_length=10, default='50')
    usb_port = db.StringField(default='/dev/cu.usbmodem1411')
    highest_air_humidity_inside = db.StringField(max_length=10, default='50')
    sleep_time_for_motors = db.StringField(max_length=10, default='30')


class Flags(db.Document):
    Motor_F = db.BooleanField(default=False)
    Motor_B = db.BooleanField(default=False)
    Motor_R = db.BooleanField(default=False)
    Motor_L = db.BooleanField(default=False)
    Fan = db.BooleanField(default=False)
    Vent = db.BooleanField(default=False)
    Door_1 = db.BooleanField(default=False)
    # Door_2 = db.BooleanField(default=False)
    Emergency_Stop = db.BooleanField(default=False)
    compost = db.ReferenceField(Devices, required=True)

    # def __str__(self):
    #     return self.Motor_F


class Measurements(db.Document):
    m_type = db.StringField(max_length=100)
    m_value = db.FloatField(max_length=6)
    # device = db.ReferenceField(Devices, required=True)
    timestamp = db.DateTimeField(default=datetime.datetime.now(), format='%d-%m-%Y')
    meta = {'max_documents': 5000}
    #
    # def __str__(self):
    #     return self.m_type

    # "soil_temp"
    # "soil_hum"
    # "air_temp"
    # "air_hum"
    # "outside_temp"
    # "outside_hum"
    # "outside_light"
    # "soil_hum"


class Log(db.Document):
    timestamp = db.DateTimeField(default=datetime.datetime.now(), format='%d-%m-%Y')
    action = db.StringField()
    meta = {'max_documents': 100}


class Errors(db.Document):
    timestamp = db.DateTimeField(default=datetime.datetime.now(), format='%d-%m-%Y')
    error = db.StringField()
    meta = {'max_documents': 100}
