
#include <stdio.h>
#include<stdlib.h>
int main()
{
    int a[10000],b[100],i,j,count=0,flag=0;
    for(i=0;i<10000;i++)
    a[i]=rand()%20000;
    for(i=0;i<100;i++)
    b[i]=rand()%20000;
    for(i=0;i<100;i++)
    {
        for(j=0;j<10000;j++)
        {
            flag++;
            if(a[i]==a[j])
            {
                count++;
                break;
            }
        }
    }
    printf("Number of searches completed is %d\n",flag);
    printf("Number of successful searches is %d\n",count);
    printf("Percentage of successful searches is %f\n",(float)((count*100)/flag));
    printf("Average number of searches per test is %d\n",(flag/count));
    return 0;
}


