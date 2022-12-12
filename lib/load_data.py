import csv


class EventTimes:
    def __init__(self):
    
        pass
    
    #Method to load in the data from the csv
    def getEvents(self,filename):
        # open the file in read mode
        fileToOpen = open(filename, 'r')

        # creating dictreader object
        file = csv.DictReader(fileToOpen)

        # creating empty list for times
        Times= []

        #Add the game times to the list and return it
        for col in file:
            Times.append(col['Game Time'])
        return Times
    

