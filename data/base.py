from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase , sessionmaker
engine = create_engine("sqlite:///tours.db")
#engine = create_engine("postgresql+psycopg2://user:2@host:port/TOUR2")


class Base(DeclarativeBase):
    pass

def create_db():
    Base.metadata.create_all(bind=engine)