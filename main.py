from Models.Birthdate import Birthdate
from Models.ImageCreator import ImageCreator

#starting point of the application#
#get the birthdate from input
print("\n+++++++++++++++++++++++++++\nWelcome to My life in weeks\n+++++++++++++++++++++++++++\n")
print("Enter your birthdate (DD-MM-YYYY): ")
try:
    birthdate = Birthdate(input())
except Exception as e:
    print("\n+++++++++++++++++++++++++++\n"+repr(e))
    print("Exit\n+++++++++++++++++++++++++++")

#create the My life in weeks calendar
imgCreator = ImageCreator(birthdate)
imgCreator.createCalendar()

