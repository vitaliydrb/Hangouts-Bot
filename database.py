from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import datetime


Base = declarative_base()
#This class will be used as table markup.
class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    name = Column(String(256))
    date = Column(Date)
    thread = Column(String(1024))
    

def create_table():
    engine = create_engine('sqlite:///ctfs.db')
    Base.metadata.create_all(engine)
    return engine


#This will check on import if database exist. And create it if not.
if not os.path.exists('ctfs.db'):
    engine = create_table()
    print('Database not found, creating')


engine = create_engine('sqlite:///ctfs.db')
Base.metadata.bind = engine
DBsession = sessionmaker(bind = engine)
session = DBsession()


#This function will add information about upcoming event to table.
def add_item(ctf, thread):
    new_ctf = Events(name=ctf.name, date=ctf.date, thread=thread)
    session.add(new_ctf)
    session.commit()


#This function will return list of events, should be reminded
def get_upcoming_events():
    tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
    items = session.query(Events).filter(Events.date == (tomorrow)).all()
    return items


#This function checks for event, that already in chat-room.
def is_unique(name):
    return session.query(Events).filter(Events.name == name).count() == 0