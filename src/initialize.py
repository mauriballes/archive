import os

from werkzeug.security import generate_password_hash

from models import create_tables, database, User

def init_db():
    # Create DB
    create_tables()

    database.connect()

    # Seed Users
    username = "admin"
    password = generate_password_hash(os.getenv("PASSWORD_ADMIN", "password"))

    User.create(username=username, password=password)

    database.close()

if __name__ == "__main__":
    init_db()