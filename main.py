from lib.load_data import EventTimes
from lib.LCDdisplay import LCDdisplay
from datetime import datetime
import pytz
from time import sleep



def main():
    # Define variables for LCD
    lcdMode = 'i2c'
    cols = 20
    rows = 4
    charmap = 'A00'
    i2cExpander = 'PCF8574'
    address = 0x27
    port = 1

    # Define run time of LCD
    runTime = 500
    
    LCD = LCDdisplay(lcdMode, cols, rows, charmap, i2cExpander, address, port)
    
    MST = pytz.timezone('America/Denver')

    CSVreader = EventTimes()

    Aves_Times = CSVreader.getEvents('AVS.csv')
    
    NUGreader = EventTimes()
    Nugs_Times = CSVreader.getEvents('NUG.csv')
    count = 0;

    

    
    while True:
        if(count < 10):
        
            NextGame = Aves_Times[0]
            Message1 = "AVALANCHE GAME AT:"
            Message2 = "STARTS IN:"
            
            datetime_MST = datetime.now(MST)
            GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
            Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
           
            
            
            while Before:
                Aves_Times.pop(0)
                NextGame = Aves_Times[0]
                GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
                Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            
            Time1 = NextGame
            TimeDiff = GameTime.replace(tzinfo=None)- datetime_MST.replace(tzinfo=None)
            Time2 = str(TimeDiff).split(".")[0]+" "
           
            
            
        else:
            if(count > 20):
                count = 0
            NextGame = Nugs_Times[0]
            Message1 = "NUGGETS GAME AT:   "
            Message2 = "STARTS IN:"
           
            datetime_MST = datetime.now(MST)
            GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
            Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            
            
            while Before:
                Nugs_Times.pop(0)
                NextGame = Nugs_Times[0]
                GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
                Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            
            Time1 = NextGame
            TimeDiff = GameTime.replace(tzinfo=None)- datetime_MST.replace(tzinfo=None)
            Time2 = str(TimeDiff).split(".")[0]+" "
           
            
            
           
        LCD.showMessageonLCD(Message1, Time1,Message2, Time2)
        count = count+1
        sleep(1)
       
        
if __name__ == "__main__":
    main()

    
