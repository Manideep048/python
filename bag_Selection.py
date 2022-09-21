
#Anita,,,6(B)
a=int(input("Enter the weight of first bag:"))
b=int(input("Enter the weight of second bag:"))
c=int(input("Enter the weight of third bag:"))
d=int(input("Enter the maximum weight of bag which is allowed for check-in:"))
e=int(input("Enter the maximum weight of bag which is allowed with her:"))
count=0
if(a+b<=d and c<=e):
    print("She has to check-in bag {} Kg and {} Kg and has to take bag {} Kg with her".format(a,b,c))
elif(a+c<=d and b<=e):
    print("She has to check-in bag {} and {} and has to take bag {} with her".format(a,c,b))
elif(b+c<=d and a<=e):
    print("She has to check-in bag {} and {} and has to take bag {} with her".format(b,c,a))
else:
    print("No possibility")


