import datetime

class Birthdate:

    def __init__(self, date):
        try:
            self.date: datetime = self.checkFormat(date)
        except:
            raise

    #checking right date format: DD-MM-YYYY#
    def checkFormat(self, date):
        try:
            return datetime.datetime.strptime(date, "%d-%m-%Y")
        except:
            raise
