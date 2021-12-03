from PIL import Image, ImageDraw, ImageFont

class ImageCreator:

    width = 2480
    height = 3508
    pathname = "Img\My life in weeks.png"

    def __init__(self, birthdate):
        #overwrite the content
        self.img = Image.new('RGB', (self.width, self.height), 'white')
        self.img.save(self.pathname)
        self.birthdate = birthdate

    #create My life in weeks calendar
    def createCalendar(self):
        #add text
        self.addText()

    #add text to image
    def addText(self):
        d = ImageDraw.Draw(self.img)
        fnt = ImageFont.truetype('Fonts\CALIST.TTF', 150)
        d.text((500,250), "MY LIFE IN WEEKS", font=fnt, fill=(0, 0, 0))
 
        self.img.save(self.pathname)

