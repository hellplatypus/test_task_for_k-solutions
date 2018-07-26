from peewee import *

from postgres import BaseModel


class Order(BaseModel):
    currency = CharField()
    amount = FloatField()
    time = DateTimeField()
    description = TextField()
