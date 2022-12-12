"""
Author: Sean Newman
"""

from RPLCD import i2c
from time import sleep

class LCDdisplay:
    def __init__(self, lcdMode, cols, rows, charmap, i2cExpander, address, port):
        # Define object variables
        self.lcdMode = lcdMode
        self.cols = cols
        self.rows = rows
        self.charmap = charmap
        self.i2cExpander = i2cExpander
        self.address = address
        self.port = port

        self.lcd = i2c.CharLCD(i2cExpander, address, port=port, charmap=charmap, cols=cols, rows=rows)

    #create a method for displaying the messages
    def showMessageonLCD(self, Title, Message,SecondTitle, SecondMessage):

        # Turn on backlight
        self.lcd.backlight_enabled = True

        # Display 1st two rows
        self.lcd.write_string(Title)
        self.lcd.crlf()
        self.lcd.write_string(Message)
        self.lcd.crlf()

        # Display 2nd two rows
        self.lcd.write_string(SecondTitle)
        self.lcd.crlf()
        self.lcd.write_string(SecondMessage)
        self.lcd.crlf()


    #Create a method to clear the screen if necessary     
    def clearScreen(self):
        # Turn on backlight
        self.lcd.backlight_enabled = True

        # Display 1st two rows
        self.lcd.clear()
