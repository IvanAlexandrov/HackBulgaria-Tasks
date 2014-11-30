from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

Base = declarative_base()


class Math(Base):
    __tablename__ = 'Players'
    id = Column(Integer, primary_key=True)
    player_name = Column(String)
    scores = Column(Integer)

# Using relative path for database via 3 slashes
engine = create_engine('sqlite:///Math.db')
Base.metadata.create_all(engine)
session = Session(bind=engine)
