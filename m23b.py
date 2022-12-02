import numpy as np
import random
def opr_1D(t):
    n=int(input("Enter the size of array1 :"))
    n1=int(input("Enter the size of array2 :"))
    if (n!=n1):
        print("NOT POSSIBLE")
    else:
        l=list()
        for i in range(n):
            val=random.randint(10,50)
            l.append(val)
        arr = np.array(l)
        l.clear()
        for i in range(n1):
            val=random.randint(10,50)
            l.append(val)
        arr1 = np.array(l)
        l.clear()
        print("******************************* ARRAY1 ***********************")
        print(arr)
        print("******************************* ARRAY2 ***********************")
        print(arr1)
        for i in range(n):
            add=arr[i]+arr1[i]
            l.append(add)
        arr2 = np.array(l)
        l.clear()
        for i in range(n):
            add=arr[i]-arr1[i]
            l.append(add)
        arr3 = np.array(l)
        l.clear()
        for i in range(n):
            multi=arr[i]*arr1[i]
            l.append(multi)
        arr4 = np.array(l)
        if t==1:
            print("************************* ARRAY ADDITION *****************")
            print(arr2)
        elif t==2:
            print("************************* ARRAY SUBTRACTION ***************")
            print(arr3)
        elif t==3:
            print("************************* ARRAY MULTIPLICATION *****************")
            print(arr4)
def opr_2D(t):
    n=int(input("Enter the size of array1 :"))
    n1=int(input("Enter the size of array2 :"))
    if n!=n1:
        print("NOT POSSIBLE")
    else:
        l1=list()
        l2=list()
        for i in range(n):
            val=random.randint(10,50)
            val1=random.randint(30,60)
            l1.append(val)
            l2.append(val1)
        arr = np.array([l1,l2])
        l1.clear()
        l2.clear()
        for i in range(n1):
            val=random.randint(10,50)
            val1=random.randint(30,60)
            l1.append(val)
            l2.append(val1)
        arr1 = np.array([l1,l2])
        l1.clear()
        l2.clear()
        print("******************************* ARRAY1 ***********************")
        print(arr)
        print("******************************* ARRAY2 ***********************")
        print(arr1)
        arr = arr.reshape(-1)
        arr1 = arr1.reshape(-1)
        for i in range(n+n1):
            add=arr[i]+arr1[i]
            l1.append(add)
        arr2 = np.array(l1)
        for i in range(n+n1):
            add=arr[i]-arr1[i]
            l2.append(add)
        arr3 = np.array(l2)
        l2.clear()
        for i in range(n+n1):
            add=arr[i]*arr1[i]
            l2.append(add)
        arr4 = np.array(l2)
        if t==1:
            print("*************************** ARRAY ADDITION ****************")
            print(arr2.reshape(2,n))
        elif t==2:
            print("*************************** ARRAY SUBTRACTION **************")
            print(arr3.reshape(2,n))
        elif t==3:
            print("*************************** ARRAY MULTIPLICATION **************")
            print(arr4.reshape(2,n))
def opr_3D(t):
    n=int(input("Enter the size of array1 :"))
    n1=int(input("Enter the size of array2 :"))
    if n!=n1:
        print("NOT POSSIBLE")
    else:
        l1=list()
        l2=list()
        l3=list()
        l4=list()
        for i in range(n):
            val=random.randint(10,50)
            val1=random.randint(30,60)
            val2=random.randint(10,20)
            val3=random.randint(20,25)
            l1.append(val)
            l2.append(val1)
            l3.append(val2)
            l4.append(val3)
        arr = np.array([[l1,l2],[l3,l4]])
        l1.clear()
        l2.clear()
        l3.clear()
        l4.clear()
        for i in range(n1):
            val=random.randint(10,50)
            val1=random.randint(30,60)
            val2=random.randint(10,20)
            val3=random.randint(20,25)
            l1.append(val)
            l2.append(val1)
            l3.append(val2)
            l4.append(val3)
        arr1 = np.array([[l1,l2],[l3,l4]])
        l1.clear()
        l2.clear()
        l3.clear()
        l4.clear()
        print("******************************* ARRAY1 ***********************")
        print(arr)
        print("******************************* ARRAY2 ***********************")
        print(arr1)
        arr = arr.reshape(-1)
        arr1 = arr1.reshape(-1)
        for i in range(4*n):
            add=arr[i]+arr1[i]
            l1.append(add)
        arr2 = np.array(l1)
        for i in range(4*n):
            add=arr[i]-arr1[i]
            l2.append(add)
        arr3 = np.array(l2)
        for i in range(4*n):
            add=arr[i]*arr1[i]
            l3.append(add)
        arr4 = np.array(l3)
        if t==1:
            print("*************************** ARRAY ADDITION *****************")
            print(arr2.reshape(2,2,n))
        elif t==2:
            print("*************************** ARRAY SUBTRACTION *****************")
            print(arr3.reshape(2,2,n))
        elif t==3:
            print("*************************** ARRAY SUBTRACTION *****************")
            print(arr4.reshape(2,2,n))
choice=1
while(choice !=0):
    print(" 1 : 1-D ARRAY")
    print(" 2 : 2-D ARRAY")
    print(" 3 : 3-D ARRAY")
    print(" 4 : Exit")
    c=int(input("Enter ur choice :"))
    if(c==1):
        k=1
        while(k!=0):
            print(" 1 : ADDITION")
            print(" 2 : SUBTRATION")
            print(" 3 : MULTIPLICATION")
            print(" 4 : Exit")
            p=int(input("Enter ur choice :"))
            if (p==1):
                opr_1D(p)
            elif (p==2):
                opr_1D(p)
            elif (p==3):
                opr_1D(p)
            elif (p==4):
                k=0
                break
            else:
                print("Enter a valid choice")
    elif(c==2):
        k=1
        while(k!=0):
            print(" 1 : ADDITION")
            print(" 2 : SUBTRACTION")
            print(" 3 : MULTIPLICATION")
            print(" 4 : Exit")
            p=int(input("Enter ur choice :"))
            if (p==1):
                opr_2D(p)
            elif (p==2):
                opr_2D(p)
            elif (p==3):
                opr_2D(p)
            elif (p==4):
                k=0
                break
            else:
                print("Enter a valid choice")
    elif(c==3):
        k=1
        while(k!=0):
            print(" 1 : ADDITION")
            print(" 2 : SUBTRACTION")
            print(" 3 : MULTIPLICATION")
            print(" 4 : Exit")
            p=int(input("Enter ur choice :"))
            if (p==1):
                opr_3D(p)
            elif (p==2):
                opr_3D(p)
            elif (p==3):
                opr_3D(p)
            elif (p==4):
                k=0
                break
            else:
                print("Enter a valid choice")
    elif(c==4):
        choice=0
        break
    else:
        print("Enter a valid choice")

