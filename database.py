from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os

Base = declarative_base()
#This class will be used as table markup.
class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    event_name = Column(String(256))
    event_date = Column(String(10))
    

def create_table():
    engine = create_engine('sqlite:///ctfs.db')
    Base.metadata.create_all(engine)

#This will check on import if database exist. And create it if not.
if not os.path.exists('ctfs.db'):
    create_table()
    print('Database not found, creating')


