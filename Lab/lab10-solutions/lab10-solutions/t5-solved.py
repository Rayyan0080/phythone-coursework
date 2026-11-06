class Point:
#    constructor
#    notice two underscores
    def __init__(self, xcoord=0, ycoord=0):
        '''initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord
        
    def get(self):
        '''(Point)->tuple
        return a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,float,float)->None
        change the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        'self == other if they have the same coordinates'
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        'return canonical string representation Point(x, y)'
        return 'Point('+str(self.x)+','+str(self.y)+')'

p1=Point(10,-1)
p2=Point(1,2)
s1="today"
a=[1,2]

# TASK 5
# how does python 'translate' each one of these calls?

#for example this one is translated as
#p1.get()
Point.get(p1)

#p2.get()
Point.get(p1)

#p1.move(1,1)
Point.move(p1,1,1)

#p1==p2
# same as p1.__eq__(p2)
# which is same as
Point.__eq__(p1,p2)

p2==p1
# same as p2.__eq__(p1)
# which is same as
Point.__eq__(p2,p1)

#s1.upper()
str.upper(s1)

#a.append(3)
list.append(a,3)
