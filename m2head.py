#M2_T1_3A
import random
n=int(input("Enter the No. of fliping :"))
head=0
tail=0
for i in range(n):
    k=random.randint(0,1)
    if(k==0):
        print("HEAD")
        head=head+1
    elif(k==1):
        print("TAIL")
        tail=tail+1
print("Number of heads is {}".format(head))
print("Number of tail is {}".format(tail))
print("Percentage of getting head is {}".format((head*100)/n))
print("Percentage of getting tail is {}".format((tail*100)/n))
