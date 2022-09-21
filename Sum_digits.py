
n=int(input("Enter the number:"))
if(n<0):
    n=-n
add=0
while(n>0):
    add=add+n%10
    n=(int)(n/10)
print("Sum of digits is {}".format(add))
    

