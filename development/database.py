from datacredentials import database, username, password, host, port

# upgraded to SQLAlchemy to handle the database connection for better compatibility and performance 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = f'postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)
# creates a database engine using SQLAlchemy

Session = sessionmaker(bind=engine)
# creating a session factory
# bind=engine associates this session factory with the previously created engine

def get_db_connection():
    return engine.connect()
# This function returns a database connection. It uses the engine object created earlier.
# When you call get_db_connection(), it establishes a connection to the database and returns the connection object. You can then use this 
# connection to execute SQL statements directly.

def get_session():
    return Session() # a session object

# /////////////////////////////////////////////


# This function returns a session object.
# When you call get_session(), it creates a new session using the session factory (Session). This session is associated with the same database connection 
# as the engine. Sessions are typically used for more complex operations that involve multiple queries or transactions.


# DATABASE = {
#     'database': database,
#     'user': username,
#     'password': password,
#     'host': host,
#     'port': port,
# }

# @contextmanager
# def get_db_connection():
#     conn = psycopg2.connect(**DATABASE)
#     try:
#         yield conn
#     finally:
#         conn.close()

# def create_table():
#     with get_db_connection() as conn:
#         with conn.cursor() as cursor:
#             cursor.execute("""
#                 DROP TABLE IF EXISTS stock_data;
#                 CREATE TABLE stock_data (
#                     id SERIAL PRIMARY KEY,
#                     symbol VARCHAR(10),
#                     date TIMESTAMP,
#                     open NUMERIC,
#                     high NUMERIC,
#                     low NUMERIC,
#                     close NUMERIC,
#                     volume BIGINT
#                 );
#             """)
#             conn.commit()

# if __name__ == '__main__':
#     create_table()

