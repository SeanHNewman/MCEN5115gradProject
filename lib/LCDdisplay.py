"""
Author: Sean Newman
"""

from RPLCD import i2c
from time import sleep

class LCDdisplay:
    def __init__(self, lcdMode, cols, rows, charmap, i2cExpander, address, port):
        """
        This constructor creates the objects for the class. It takes
        in the information needed to establish the i2c communication
        for the LCD.
        Input:  lcdMode <str> - Defines communication protocal
                cols <int> - Number of columns on the LCD
                rows <int> - Number of rows on the LCD
                charmap <str> - Character mapping for LCD
                i2cExpander <str> - i2c expander information
                address <hex> - Hex address for i2c comms
                port <int> - raspberry pi port number
        Output: None
        """
        # Define object variables
        self.lcdMode = lcdMode
        self.cols = cols
        self.rows = rows
        self.charmap = charmap
        self.i2cExpander = i2cExpander
        self.address = address
        self.port = port

        self.lcd = i2c.CharLCD(i2cExpander, address, port=port, charmap=charmap, cols=cols, rows=rows)


    def showMessageonLCD(self, Title, Message,SecondTitle, SecondMessage):

        # Turn on backlight
        self.lcd.backlight_enabled = True

        # Display 1st two rows
        self.lcd.write_string(Title)
        self.lcd.crlf()
        self.lcd.write_string(Message)
        self.lcd.crlf()

        # Display 1st two rows
        self.lcd.write_string(SecondTitle)
        self.lcd.crlf()
        self.lcd.write_string(SecondMessage)
        self.lcd.crlf()

        # Sleep between
        
    def clearScreen(self):
        # Turn on backlight
        self.lcd.backlight_enabled = True

        # Display 1st two rows
        self.lcd.clear()
