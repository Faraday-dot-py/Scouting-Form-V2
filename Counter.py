import tkinter as tk

class countChanger():
    def __init__(self, widgetTitle, amount, items, maxCount, minCount):
        self.widgetTitle = widgetTitle
        self.amount = amount
        self.items = items
        self.value = tk.IntVar()
        self.value.set(0)
        self.maxCount = maxCount
        self.minCount = minCount
        
    def incrementCount(self):
        val = self.value.get()
        for i in self.items:
            if i[0] == self.widgetTitle:
                if val < self.maxCount:                    
                    self.value.set(val + self.amount)
                    print(self.widgetTitle + ": " + str(val))
                
    def decrementCount(self):
        val = self.value.get()
        for i in self.items:
            if i[0] == self.widgetTitle:
                if val > self.minCount:                    
                    self.value.set(val - self.amount)
                    print(self.widgetTitle + ": " + str(val))
