'''
Author:Kalpana Baigar
Program to accept the numbers and return the frequency of even numbers
'''

list=[]

for i in range(0,5):
    data=int(input("enter number"))
    list.append(data)
print(list)    




count=0
for i in range(0,5):
    if(list[i]%2==0):
        count+=1


print("frequency of even number is: {} ".format(count))
    
