"""
Author:Kalpana Baigar
Progarm to check frequency of number
"""

import array as arr

'''
a=arr.array('i',[2,3,4,4,4,6])

x=4
frequency=a.count(x)
print("frequency of number {0} is {1}".format(x,frequency))
'''

a=['i']
size=int(input("enter size of an array:"))
no=int(input("enter number to check frequency:"))


def frequency(b,num,siz):
    count=0
    for i in range(0,siz+1):
        if(b[i]==num):
           print("hii")
           count+=1 
    return count

    
def display(b,siz):
    for i in range(0,siz+1):
        x=int(input("enter element"))    
        b.append(x)
    print(b)


display(a,size)


a=frequency(a,no,size)
print("frequency is {}:".format(a))












