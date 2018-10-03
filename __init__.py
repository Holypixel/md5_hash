from celery import Celery
from sqlalchemy import SQLAlchemy
from marshmallow import Marshmallow
from md5_hash_light.api import app
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'app'


celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)
db = SQLAlchemy(app)
ma = Marshmallow(app)

