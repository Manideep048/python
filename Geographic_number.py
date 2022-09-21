
import math
k=1
while(k!=0):
    print("1.Circle")
    print("2.Rectangle")
    print("3.Triangle")
    print("4.Exit")
    choice=int(input("Enter your choice:"))
    if(choice==1):
        r=abs(int(input("Enter the radius of circle:")))
        area=(float)(3.14*math.pow(r,2))
        print("Area of circle is {}".format(area))
    elif(choice==2):
        l=abs(int(input("Enter the length of rectangle")))
        b=abs(int(input("Enter the width of rectangle")))
        area=l*b
        print("Area of rectangle is {}".format(area))
    elif(choice==3):
        a=abs(int(input("Enter the first side of triangle")))
        b=abs(int(input("Enter the second side of triangle")))
        c=abs(int(input("Enter the third side of triangle")))
        s=(float)((a+b+c)/2)
        area=(float)(math.sqrt(s*(s-a)*(s-b)*(s-c)))
        print("Area of triangle is {}".format(area))
    elif(choice==4):
        break

