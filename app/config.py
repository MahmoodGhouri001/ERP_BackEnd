import os
class databaseconfig:
    db_username = os.environ["db_username"]
    db_password = os.environ["db_password"]
    db_hostname = os.environ["db_hostname"]
    db_name = os.environ["db_name"]
    SQLALCHEMY_DATABASE_URI = f"mysql://{db_username}:{db_password}@{db_hostname}/{db_name}"
