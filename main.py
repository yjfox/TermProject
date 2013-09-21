import csv
import copy
from collections import OrderedDict

class dataanalytics(object):
    def __init__(self, trainPath):
        self.trainPath = trainPath
        self.data = []
    
    
    
    
    def readData(self):
        file = open(self.trainPath,'rU')
        raw = csv.reader(file)
        names = raw.next() # The first line is used for store keys for the self.data
        datarow = {} # datarow is used to store: X, Y, Z, T, and Device
        for row in raw:
            datarow[names[0]] = row[0]
            datarow[names[1]] = row[1]
            datarow[names[2]] = row[2]
            datarow[names[3]] = row[3]
            datarow[names[4]] = row[4]
            print datarow
            self.data.append(copy.copy(datarow))
        print self.data[0]

        
if __name__=='__main__':
    path = 'train.csv'
    
    w = dataanalytics(path)
    w.readData()