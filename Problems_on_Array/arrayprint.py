"""
Author: Kalpana Baigar
Program to accept N numbers using array and passing that aray to function and printing
values in that array 
"""

import array as arr

a=arr.array('i')


size=int(input("enter size of an array"))


for i in range(size):
    x=int(input("enter value"))
    a.append(x)



def display(j,no):       #printing array element
    print(j)


display(a,size)



"""
value=3
for i in range(size):   # check number 2 is present or not
    if(a[i]==value):
       print("found")
       break
else:
    print("not found") 
"""
