import tkinter as tk
from tkinter import ttk
import Converter
import Counter
import Submitter

class Widget:
    
    def __init__(self, screenHeight, screenWidth, formTitle, backgroundColor, textColor, itemColor):
        
        self.backgroundColor = backgroundColor
        
        self.textColor = textColor
        
        self.screenHeight = screenHeight
        
        self.screenWidth = screenWidth
        
        self.items = []
        
        self.form = tk.Tk()

        self.form.title(formTitle)
        
        self.formTitle = formTitle

        self.form.configure(width = screenWidth, height = screenHeight)

        self.form.resizable(False, False)

        self.form.configure(bg = backgroundColor)
        
        self.cv = Converter.Converter(screenWidth, screenHeight)
        
        
        
        
    def createTextInput(self, text, xPos, yPos):
        value = tk.StringVar()
        self.items.append([text,
                       tk.Label(self.form, text = text, bg = self.backgroundColor, fg = self.textColor),
                       tk.Entry(self.form, width = int(len(text) + (0.3 * len(text))), textvariable = value),
                       value

                       ]
                      )
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos))
        self.items[len(self.items)-1][2].place(relx = self.cv.toPercent(width = xPos - int(0.15*len(text))), rely = self.cv.toPercent(height = yPos + 20))

        
    def createBoolean(self, text, xPos, yPos):
        value = tk.IntVar;
        self.items.append([text,
                       tk.Checkbutton(self.form, text = text, bg = self.backgroundColor, fg = self.textColor, selectcolor = self.backgroundColor, variable = value, onvalue = 1, offvalue = 0),
                       value
                       
                       ]
                      )
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos))
        
    def createLabel(self, text, xPos, yPos):
        self.items.append([text,
                       tk.Label(self.form, text = text, bg = self.backgroundColor, fg = self.textColor),
                       None
                       ]
                      )
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos))
        
    def createCounter(self, text, changeValue, xPos, yPos, maxCount = 256, minCount = -256):

        counter = Counter.countChanger(text, changeValue, self.items, maxCount, minCount)

        value = counter.value

        self.items.append([text,

                        tk.Label(text = text, bg = self.backgroundColor, fg = self.textColor),

                        tk.Label(textvariable = counter.value, bg = self.backgroundColor, fg = self.textColor),

                        0,

                        tk.Button(text = "Increase", command = counter.incrementCount),

                        tk.Button(text = "Decrease", command = counter.decrementCount),

                        value
                      ]
                     )

        for i in self.items:
            print(i)
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos - len(text)*4), rely = self.cv.toPercent(height = yPos))
        self.items[len(self.items)-1][2].place(relx = self.cv.toPercent(width = xPos - 5), rely = self.cv.toPercent(height = yPos + 25))
        self.items[len(self.items)-1][4].place(relx = self.cv.toPercent(width = xPos + 30), rely = self.cv.toPercent(height = yPos + 35))
        self.items[len(self.items)-1][5].place(relx = self.cv.toPercent(width = xPos - 80), rely = self.cv.toPercent(height = yPos + 35))
    
    def createDropdown(self, text, xPos, yPos, dropdownOptions):
        value = tk.StringVar()
        maxLen = 0
        
        for i in dropdownOptions:
            if len(str(i)) > maxLen:
                maxLen = len(str(i))
                
        self.items.append([text,
                      tk.Label(text = text),
                      ttk.Combobox(self.form, width = maxLen + 1, textvariable = value),
                      value
                      ]
                     )
#         test = tk.Label(text = text, bg = self.backgroundColor, fg = self.textColor)
#         
#         
#         test.place(relx = xPos, rely = yPos)

        self.items[len(self.items)-1][2]["values"] = dropdownOptions
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos))
        self.items[len(self.items)-1][2].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos + 20))
    
    def createSubmitButton(self, xPos, yPos, text = "Submit"):
        
        headers = []
        
        for i in self.items:
            headers.append(i[0])

        headers.append(text)
            
        # print(headers)
        
        submitter = Submitter.Submitter(headers, self.formTitle, self)

        
        self.items.append([text,
                           tk.Button(text = text, command = submitter.saveData),
                           None
                          ]
                         )
        # print(self.items)
        # print("\n\n")
        # print(self.items[len(self.items)-1])
        # print("\n\n")
        # print(self.items[len(self.items)-1][2])
        
        self.items[len(self.items)-1][1].place(relx = self.cv.toPercent(width = xPos), rely = self.cv.toPercent(height = yPos + 20))



    def __getData(self):
        data = []

        for i in self.items:

            data.append(i[len(i)-1])

        return data
        
    
    
    def createForm(self):
        self.form.mainloop()
        