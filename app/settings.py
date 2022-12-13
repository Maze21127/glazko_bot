import os
from dotenv import load_dotenv

load_dotenv('.env')

BOT_TOKEN = os.getenv('BOT_TOKEN')

SQLALCHEMY_DATABASE_URI = 'sqlite:///app_db.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.urandom(20)
FLASK_ADMIN_SWATCH = 'cosmo'
BABEL_DEFAULT_LOCALE = 'ru'
