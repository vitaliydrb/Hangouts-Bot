import datetime
from dateutil import parser


#Thiss class will create object for each event.
class CTF(object):


    def __init__(self, name, link, beginning):
        self.name = name
        self.link = link
        self.beginning = beginning
        self.date = parser.parse(self.beginning)


#This function will check if event will begin in ~3 weeks.
    def get_eta(self):        
        if self.date.year == datetime.date.today().year:
            if datetime.date.today().day < 30:
                if self.date.month == datetime.date.today().month:
                    return True
                elif (self.date.month -1 == datetime.date.today().month) and (self.date.date < 16):
                    return True