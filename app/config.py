class databaseconfig:
    db_username = "admin"
    db_password = "Root1234"
    db_hostname = "erp-database.cd17exehpjhk.us-west-2.rds.amazonaws.com"
    db_name = "ERP_SYSTEM"
    SQLALCHEMY_DATABASE_URI = f"mysql://{db_username}:{db_password}@{db_hostname}/{db_name}"
