import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Connect to the database
username="postgres"
password="postgres"
host="localhost"
port=5432
database_name="fyyur"

# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(username, password, host, port,database_name)
