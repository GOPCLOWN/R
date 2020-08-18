from peewee import *
from playhouse.sqliteq import SqliteQueueDatabase

db = SqliteQueueDatabase("database/db.db")


class Global(Model):
    id = PrimaryKeyField(null=False)
    user_id = IntegerField(null=False)
    balance = IntegerField(default=0)
    license = DateTimeField(default='')
    adm = BooleanField(default=False)

    class Meta:
        db_table = 'Users'
        database = db


class WhiteNumber(Model):
    id = PrimaryKeyField(null=False)
    number = IntegerField(null=False)
    user_id = IntegerField(null=False)

    class Meta:
        db_table = 'Numbers'
        database = db


def con():
    try:
        db.connect()
        Global.create_table()
        print('База данных Users успешно загружена')
    except InternalError as px:
        print(str(px))
        raise
    try:
        WhiteNumber.create_table()
        print('База данных Numbers успешно загружена')
    except InternalError as px:
        print(str(px))
        raise