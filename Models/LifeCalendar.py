from datetime import date, datetime, timedelta
import os
from PIL import Image, ImageDraw, ImageFont
import calendar
from Models.Birthdate import Birthdate

class LifeCalendar:

    #image dimension

    #A4
    width = 2480
    height = 3508

    #A3
    #width = 3508
    #height = 4961

    imageName = "My life in weeks.png"
    pathnameImage = "Img\\" + imageName
    pathnameFont = "Fonts\CALIST.TTF"

    #misures in pixels
    numberTextPixelsStartingError = 7

    titleFontSize = 100
    numberFontSize = 34
    oneDigitNumberWidth = 27
    twoDigitNumberWidth = 45

    startTextPosition = (750,50)
    startSquaresPositionX = 250
    startSquaresPositionY = 200

    squaresDimension = 25
    squaresMargin = 10
    spaceBetweenMonthsYears = 10

    years = 90

    def __init__(self, birthdate: Birthdate):
        #overwrite the content
        self.img = Image.new('RGB', (self.width, self.height), 'white')
        self.img.save(self.pathnameImage)
        self.birthdate = birthdate

    #create My life in weeks calendar
    def fillCalendar(self):
        #add title on Calendar
        self.addTitle()

        #add squares on Calendar
        self.addSquares()

        #add numbers on Calendar
        self.addNumbers()

    #add title to image
    def addTitle(self):
        d = ImageDraw.Draw(self.img)
        fnt = ImageFont.truetype(self.pathnameFont, self.titleFontSize)
        d.text(self.startTextPosition, "MY LIFE IN WEEKS", font=fnt, fill=(0, 0, 0))
 
        self.img.save(self.pathnameImage)

    #add squares to image
    def addSquares(self):
        endMonthFlag = 0
        endTenYearFlag = 0

        for y in range(self.years):
            for x in range(52):
            
                #space between months
                if ((x != 0) & (x % 4 == 0)):
                    endMonthFlag += 1

                #space between years
                #(y/10 != endTenYearFlag) because it needs to increment only one time when (y % 10 == 0)
                if ((y != 0) & (y % 10 == 0) & (y/10 != endTenYearFlag)):
                    endTenYearFlag += 1

                positionX = self.startSquaresPositionX + x * (self.squaresMargin + self.squaresDimension) + endMonthFlag * self.spaceBetweenMonthsYears 
                positionY = self.startSquaresPositionY + y * (self.squaresMargin + self.squaresDimension) + endTenYearFlag * self.spaceBetweenMonthsYears

                #choose black or white square
                isBlack = self.isBlackSquare(x, y)
                if (isBlack):
                    color = 'black'
                else: 
                    color = 'white'

                #draw the square
                #positionX, positionY is the left top corner
                self.drawSquare(positionX, positionY, color)

            endMonthFlag = 0

        self.img.save(self.pathnameImage)

    # week = range [0, 51]
    # year = range [0, 89]
    def isBlackSquare(self, week, year):

        todayDate = datetime.today()
        datePointed = self.birthdate.date

        """Return a date that's `year` years after the date (or datetime)
        object `datePointed`. Return the same calendar date (month and day) in the
        destination year, if it exists, otherwise use the following day
        (thus changing February 29 to March 1).
        """
        try:
            datePointed = datePointed.replace(year = datePointed.year + year)
        except ValueError:
            datePointed = datePointed + (date(datePointed.year + year, 1, 1) - date(datePointed.year, 1, 1))

        datePointed = datePointed + timedelta(weeks = week + 1)

        return datePointed < todayDate


    #draw the image
    def drawSquare(self, positionX, positionY, color):
        d = ImageDraw.Draw(self.img)
        #(x0,y0) is the left top corner of the rectangle
        #(x1,y1) is the rigth bottom corner of the rectangle
        d.rectangle((
            #x0
            positionX,
            #y0 
            positionY,
            #x1
            positionX + self.squaresDimension,
            #y1 
            positionY + self.squaresDimension), 
            #border color
            outline='black',
            #square color
            fill=color,
            #The line width, in pixels
            width=2)

    def addNumbers(self):
        endTenYearFlag = 0
        for y in range(self.years):
            #space between years
            #(y/10 != endTenYearFlag) because it needs to increment only one time when (y % 10 == 0)
            if ((y != 0) & (y % 10 == 0) & (y/10 != endTenYearFlag)):
                endTenYearFlag += 1

            positionY = self.startSquaresPositionY + y * (self.squaresMargin + self.squaresDimension) + endTenYearFlag * self.spaceBetweenMonthsYears - self.numberTextPixelsStartingError

            #right alignment for numbers with one digit
            if (y < 10):
                positionX = self.startSquaresPositionX - self.oneDigitNumberWidth
            else:
                positionX = self.startSquaresPositionX - self.twoDigitNumberWidth
            
            if (y%5 == 0):
                d = ImageDraw.Draw(self.img)
                fnt = ImageFont.truetype(self.pathnameFont, self.numberFontSize)
                d.text((
                    positionX,
                    positionY
                    ), str(y), font=fnt, fill=(0, 0, 0))
        
        self.img.save(self.pathnameImage)

    def saveToDesktop(self):
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
        self.img.save(desktop + '\\' + self.imageName)