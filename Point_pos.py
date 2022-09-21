
import math
x1=int(input("Enter the first centre coordinate:"))
y1=int(input("Enter the second centre coordinate:"))
x2=int(input("Enter the first point coordinate:"))
y2=int(input("Enter the second point coordinate:"))
r=int(input("Enter the radius:"))
d=math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
if(d<r):
    print("Point({},{}) lies inside circle".format(x2,y2))
elif(d>r):
    print("Point({},{}) lies outside circle".format(x2,y2))
elif(d==r):
    print("Point({},{}) lies on circle".format(x2,y2))

