
#Guessing Number,,,5(A)
import random
k=1
count=0
a=random.randint(1,1000)
while(k<=10):
    n=int(input("Enter ur number:"))
    if(n==a):
        print("You had guessed correct")
        print(n)
        count=count+1
    else:
        if((a-n)<0):
            t=-(a-n)
        else:
            t=a-n
        if(t<=50):
            print("You are too near")
        else:
            print("You are too far away")
    k=k+1
print("Your score is {}".format(count))


