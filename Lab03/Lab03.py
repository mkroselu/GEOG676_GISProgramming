# Class Definition 

class Shape():
    def __init__(self):
        pass

    def getArea(self):
        pass 

class Rectangle(Shape):
    def __init__(self, l, w):
        super().__init__()
        self.l = l
        self.w = w

    def getArea(self):
        return self.l * self.w 

class Triangle(Shape):
    def __init__(self, b, h):
        super().__init__()
        self.b = b
        self.h = h

    def getArea(self):
        return self.b * self.h /2

class Circle(Shape): 
    def __init__(self, r):
        super().__init__()
        self.r = r

    def getArea(self):
        return 3.14 * self.r**2 

# Read txt file 

file = open(r'C:\Users\MEI-KUEI LU\Downloads\GEOG676_GIS_Programming\Lab\GEOG676_GISProgramming\Lab03\shape.txt')
lines = file.readlines()
file.close()

##print(lines[0].split(',')[2])
##print(Rectangle(2,4).getArea()) 

shape_list = []

for line in lines:
    components = line.split(',')
    shape = components[0]

    if shape == 'Rectangle':
        x = float(components[1])
        y = float(components[2])
        shape_list.append(Rectangle(x, y))
    
    elif shape == 'Triangle':
        x = float(components[1])
        y = float(components[2])
        shape_list.append(Triangle(x, y))
        
    elif shape == 'Circle':
        x = float(components[1])
        shape_list.append(Circle(x))
        
    else: 
        pass 

for shape in shape_list: 
    print(shape.getArea())
    

