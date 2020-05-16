"""
Author:Kalpana Baigar
Program to accept N numbers from user ,and check wether one another number is present or not
"""

import array as arr

arraynum=arr.array('i',[1,2,3,4])
value=7

def check(x,no):
    for b in range(0,4):
         if(x[b]==no):
           print(" number {} is found".format(value))
           break
    else:
        print(" number {} is not found".format(value))
        
check(arraynum,value)

