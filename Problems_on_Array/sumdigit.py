'''
Author:Kalpana Baigar
Program to printing summation of digits
'''

list=[]

size=int(input("enter range"))

print("enter elements")
for i in range(0,size):    #accepting elements from user
    data=int(input())
    list.append(data)

print(list)               #printing list

length=len(list)

for i in range(length):   #iterating the list
    no=list[i]
    temp=no
    sum=0
    while(no>0):          
        digit=no%10
        sum=sum+digit
        no=no//10
    print("number {0} having digit summation is:{1}".format(temp,sum))
