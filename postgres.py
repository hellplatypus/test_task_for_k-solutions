from peewee import *
from urllib.parse import urlparse

from app.config import DB_CREDENTIALS

result = urlparse(DB_CREDENTIALS)

db = PostgresqlDatabase(user=result.username, password=result.password, database=result.path[1:], host=result.hostname)


class BaseModel(Model):
    class Meta:
        database = db
