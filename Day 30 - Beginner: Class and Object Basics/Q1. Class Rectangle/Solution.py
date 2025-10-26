class Rectangle:
    # Define properties here
    #Length  = 0
    #Breadth = 0
    
    
    # Define constructor here
    def __init__(self,Length,Breadth):
        self.Length  = Length 
        self.Breadth = Breadth 


    def perimeter(self):
        # Complete the function
        return 2*(self.Length+self.Breadth)
    
    
    def area(self):
        # Complete the function
        return self.Length*self.Breadth
    
        
#Rectangle a = new Rectangle(2, 3) 
#a.perimeter() 
#a.area()  