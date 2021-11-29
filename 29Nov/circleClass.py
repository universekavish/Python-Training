class Circle :
    def __init__(self, x, y, z) :
        self.xCord = x
        self.yCord = y
        self.radius = z
	
    def __str__(self) :
        return 'Circle(({0}, {1}), {2})'.format(self.xCord, self.yCord, self.radius)
		
    def circumference(self) :
        return 2*(22/7)*(self.radius)
		
    def area(self) :
        return (22/7)*(self.radius)*(self.radius)
		
    def centralAngle(self, l) :
        return 360*(l/circumference)
		
    def areaOfSector(self, angle) :
        return (angle/360)*(22/7)*(self.radius)*(self.radius)
		
    def __eq__(self, other) :
        return self.xCord == other.xCord and self.yCord == other.yCord and self.radius == other.radius
    
    def __add__(self, other) :
        temp = Circle(self.xCord + other.xCord, self.yCord + other.yCord, self.radius + self.radius)
        return temp
    	
    def scale(self, radius = 0) :
        if self.radius + radius > 0 :
            self.radius = self.radius + radius 	
        else : 
            print('Scaling not allowed ')
			
    def move(self, xCord = 0, yCord = 0) :
        self.xCord = self.xCord + xCord
        self.yCord = self.yCord + yCord
	
#Main App Begins Here
C1 = Circle(2, 3, 7)
print(C1)

#1. circumference
circumference = C1.circumference()
print('Circumference : ', circumference)

#2. area
area = C1.area()
print('Area : ', area)

#3. centralAngle
centralAngle = C1.centralAngle(11)
print('centralAngle : ', centralAngle)

#4. areaOfSector
areaOfSector = C1.areaOfSector(90)
print('areaOfSector : ', areaOfSector)

#5. Same or not
C2 = Circle(3, 4, 7)
if C1 == C2 : 
	print('Same circle')
else : 
	print('not same circle ')
	
#6. Scaling
result = C1.scale(radius = 3)
print('Scaled ', C1)

#7. Moving
result1 = C1.move(xCord = 3, yCord = 3)
print('Moved ', C1)

#8. Add 
C3 = C1 + C2
print(C3)