import datetime
from dateutil import parser
from bot import send_message


class CTF:

    def __init__(self, name, link, beginning):
        self.name = ''
        self.link = ''
        self.beginning = ''
        self.date = parser.parse(self.beginning)
            
    def get_eta(self):        
        if self.date.year == datetime.date.today().year:
            if datetime.date.today().day < 23:
                if self.date.month == datetime.date.today().month:
                    send_message(self)
            elif self.date.date < 15:
                if ((self.date.month) -1) == datetime.date.today().month:
                    send_message(self)