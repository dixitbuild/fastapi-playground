from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://dixitdhiman:12345678@localhost:5432/dixitdhiman"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflus=False, bind=engine)