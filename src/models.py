from peewee import *

DATABASE = 'videos.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database


class Video(BaseModel):
    name = CharField()
    link = CharField()


def create_tables():
    with database:
        database.create_tables([Video,])