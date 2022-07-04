import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


user = os.environ['coinjet_db_user']
password = os.environ['coinjet_db_password']
host = os.environ['coinjet_db_host']
db_name = os.environ['coinjet_db_dbname']


# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL =  "postgresql://{}:{}@{}/{}".format(user, password, host, db_name)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()