class Converter:
    def __init__(self, screenHeight, screenWidth):
        
        self.screenHeight = screenHeight
        
        self.screenWidth = screenWidth
    
    def toPercent(self, height = None, width = None):
        if height == None:
            
            return width / self.screenWidth
        
        elif width == None:
            
            return height / self.screenHeight
        
        else:
            
            return width / self.screenWidth, height / self.screenHeight
    
    def toPixels(self, height = None, width = None):
        if height == None:
            
            return self.width * (width / 100)
        
        elif width == None:
            
            return self.height * (height / 100)
        
        else:
            
            return self.width * (width / 100), self.height * (height / 100)
        

