
#Room-rent,,,,,5(B)
x=int(input("Enter the cost of Double room:"))
y=int(input("Enter the cost of Triple room:"))
if((3*x)<(2*y)):
    print("They have to book Double room and have to spend minimum Rs {}".format(3*x))
else:
    print("They have to book Triple room and have to spend minimum Rs {}".format(2*y))

