from peewee import *

DATABASE = 'videos.db'

database = SqliteDatabase(DATABASE)

class BaseModel(Model):
    class Meta:
        database = database

class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()


class Video(BaseModel):
    name = CharField()
    description = CharField()
    yt_id = CharField()
    embed_link = CharField()
    thumbnail_link = CharField()


def create_tables():
    with database:
        database.create_tables([User, Video,])