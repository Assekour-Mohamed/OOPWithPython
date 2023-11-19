class Rec:
    # def __init__(self):
    #     self.width = 0
    #     self.hieght = 0
    def __init__(self, width, hieght):
        self.width = width
        self.hieght = hieght
    # def __init__(self, R1):
    #     self.width = R1.width
    #     self.hieght = R1.hieght
    
    def perimetre(self):
        return 2 * (self.width + self.hieght)
    
    def Aire(self):
        return self.width * self.hieght
    
    def IsCarre(self):
        if self.width == self.hieght:
            return "il s'agait d'un carre."
        else:
            return "il ne s'agait pas d'un carre."
    
    def AfficherRectangle(self):
        print("hight :", self.hieght)
        print("widht :", self.width)
        print("premitre : ", self.perimetre())
        print("is carre : ", self.IsCarre())
    

