from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


config = {
    'User': 'postgres',
    'Password': '1234',
    'Host': 'localhost',
    'Port': '5432',
    'Database': 'postgres'
}

engine = create_engine(f'postgresql+psycopg2://{config["User"]}:{config["Password"]}@{config["Host"]}:{config["Port"]}/{config["Database"]}')

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
