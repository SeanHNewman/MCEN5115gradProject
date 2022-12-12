import csv


class EventTimes:
    def __init__(self):
    
        pass
    
    def getEvents(self,filename):
        # open the file in read mode
        fileToOpen = open(filename, 'r')

        # creating dictreader object
        file = csv.DictReader(fileToOpen)

        # creating empty lists
        Times= []

        # iterating over each row and append
        # values to empty list
        for col in file:
            Times.append(col['Game Time'])
        return Times
    

