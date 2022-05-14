import csv
import os
import tkinter as tk
from datetime import datetime

class Submitter:
    def __init__(self, headers, fileName, widgetClass):
        
        now = datetime.now()

        folder = r"Saves\\"
        
        self.fileName = folder[:len(folder)-1] + fileName + str(now.strftime("--%Y%m%d_%H_%M_%S")) + ".csv"

        self.widgetClass = widgetClass
        
        saveFile = open(self.fileName, mode = "w")
        
        saveWriter = csv.writer(saveFile)
            
        saveWriter.writerow(headers)
            
        saveFile.close()
        
    def saveData(self):

        data = []

        for i in self.widgetClass.items:

            val = i[len(i)-1]

            print(val, type(val))


            if type(val) is int:

                data.append(val)

            elif val != None:
                #WORK HERE ----------------

                data.append(val.get())

            else:
                data.append("None")

        with open(self.fileName, mode='a') as saveFile:

            saveWriter = csv.writer(saveFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            # print("-----", data, len(data))
            
            saveWriter.writerow(data)
                
            saveFile.close()
    
            
