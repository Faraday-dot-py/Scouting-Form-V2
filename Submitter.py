import csv
import os
from datetime import datetime

class Submitter:
    def __init__(self, headers, fileName):
        
        now = datetime.now()

        folder = r"Saves\\"
        
        self.fileName = folder[:len(folder)-1] + fileName + str(now.strftime("--%Y%m%d_%H_%M_%S")) + ".csv"
        
        
        saveFile = open(self.fileName, mode = "w")
        
        saveWriter = csv.writer(saveFile)
            
        saveWriter.writerow(headers)
            
        saveFile.close()
        
        self.data = []
    
    def setData(self, data):
        
        for i in data:
            if i != None:
                self.data.append(i.get())
            else:
                self.data.append("None")
                
        
        print(data)
        
    def saveData(self):
        with open(self.fileName, mode='a') as saveFile:
            saveWriter = csv.writer(saveFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            
            print(self.data, len(self.data))
            
            saveWriter.writerow(self.data)
                
            saveFile.close()
        
        self.data = []
    
            
