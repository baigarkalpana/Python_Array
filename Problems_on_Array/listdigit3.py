'''
Author:Kalpana Baigar
Program to dispaly that numbers only which contains 3 digits
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
    cnt=0
    while(no>0):          
        digit=no%10
        cnt+=1
        no=no//10
    if(cnt==3):
        print("number {0} having digit 3".format(temp))
