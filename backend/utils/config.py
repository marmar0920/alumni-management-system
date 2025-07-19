import os 
from dotenv import load_dotenv
load_dotenv()

class Config:
    SECRET_KEY = 'replace_this_with_a_random_secret'
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:mardnie@localhost/alumnidb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
