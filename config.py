import os

DEBUG = True
SECRET_KEY = os.urandom(128)

# DATABASE CONFIG
MONGODB_DB = 'compost'
MONGODB_HOST = 'ds127190.mlab.com'
MONGODB_PORT = 27190
MONGODB_USERNAME = 'yannis'
MONGODB_PASSWORD = 'spacegr'
