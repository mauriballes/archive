import os

from peewee import *

DATABASE_NAME = os.getenv('DB_NAME', 'archive_videos')
DATABASE_USER = os.getenv('DB_USER', 'postgres')
DATABASE_PASS = os.getenv('DB_PASS', '')
DATABASE_HOST = os.getenv('DB_HOST', 'localhost')
DATABASE_PORT = os.getenv('DB_PORT', 5432)

database = PostgresqlDatabase(
    DATABASE_NAME, user=DATABASE_USER, password=DATABASE_PASS, 
    host=DATABASE_HOST, port=DATABASE_PORT)

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