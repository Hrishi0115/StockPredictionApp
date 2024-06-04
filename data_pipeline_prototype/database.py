# this file will manage the database connections and sessions

# backend/database.py

from datacredentials import database, username, password, host, port
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

def get_db_connection():
    return engine.connect()

def get_session():
    return Session()
