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
    
    #Define the Timezone
    MST = pytz.timezone('America/Denver')

    #Create an instance of the CSV reader and load in the times
    CSVreader = EventTimes()
    Aves_Times = CSVreader.getEvents('AVS.csv')
    Nugs_Times = CSVreader.getEvents('NUG.csv')
    #Define a countavariable to be used later
    count = 0;

    

    #Run indefinitely 
    while True:
        #pull the current time
        datetime_MST = datetime.now(MST)
        if(count < 10):
            
            #Pull the next game and define some messages
            NextGame = Aves_Times[0]
            Message1 = "AVALANCHE GAME AT:"
            Message2 = "STARTS IN:"
            
            #convert to a datetime type and check if the game is in the past
            GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
            Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
           
            
            #if the game is in the past remove it and check the next game, repeat until all past games are gone
            while Before:
                Aves_Times.pop(0)
                NextGame = Aves_Times[0]
                GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
                Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            #create the messages for display
            Time1 = NextGame
            TimeDiff = GameTime.replace(tzinfo=None)- datetime_MST.replace(tzinfo=None)
            Time2 = str(TimeDiff).split(".")[0]+" "
           
            
            
        else:
            #reset the counter
            if(count > 20):
                count = 0
            #Pull the next game and define some messages    
            NextGame = Nugs_Times[0]
            Message1 = "NUGGETS GAME AT:   "
            Message2 = "STARTS IN:"

            #convert to a datetime type and check if the game is in the past
            GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
            Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            
            #if the game is in the past remove it and check the next game, repeat until all past games are gone
            while Before:
                Nugs_Times.pop(0)
                NextGame = Nugs_Times[0]
                GameTime = datetime.strptime(NextGame, "%Y.%m.%d-%H:%M")
                Before = (datetime_MST.replace(tzinfo=None) > GameTime.replace(tzinfo=None))
            
            #create the messages for display
            Time1 = NextGame
            TimeDiff = GameTime.replace(tzinfo=None)- datetime_MST.replace(tzinfo=None)
            Time2 = str(TimeDiff).split(".")[0]+" "
           
            
            
        #Display the messaage then wait 1 second   
        LCD.showMessageonLCD(Message1, Time1,Message2, Time2)
        count = count+1
        sleep(1)
       
        
if __name__ == "__main__":
    main()

    
