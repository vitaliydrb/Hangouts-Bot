from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()
#This class will be used as table markup.
class Events(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key = True)
    event_name = Column(String(256))
    event_date = Column(String(10))
    thread_id = Column(String(1024))
    

def create_table():
    engine = create_engine('sqlite:///ctfs.db')
    Base.metadata.create_all(engine)
    return engine

#This will check on import if database exist. And create it if not.
if not os.path.exists('ctfs.db'):
    engine = create_table()
    print('Database not found, creating')


#This function will add information about upcoming event to table.
def add_item(ctf, thread):
    Base.metadata.bind = engine
    DBsession = sessionmaker(bind = engine)
    session = DBsession()
    new_ctf = Events(name=ctf.name, date='{} {} {}'.format(ctf.date.year, ctf.date.month, ctf.date.day), thread_id=thread)
    session.add(new_ctf)
    session.commit()

