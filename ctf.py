import datetime
from dateutil import parser


#Thiss class will create object for each event.
class CTF(object):


    def __init__(self, name, link, beginning):
        self.name = name
        self.link = link
        self.beginning = beginning
        self.datetime = parser.parse(self.beginning)
        self.date = self.datetime.date()


#This function will check if event will begin in ~3 weeks.
    def get_eta(self):
        three_weeks = datetime.timedelta(days = 21)
        today = datetime.date.today()
        if (self.date <= (today + three_weeks)) and self.date >= today:
            return True