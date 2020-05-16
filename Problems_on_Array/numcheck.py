'''
Author:Kalpana Baigar
Program to accept the numbers and and check 11 number is present or not
'''

list=[11,12,13,14]
num=11

def check(lst,no):
    value=0
    for i in range(0,4):
        if(lst[i]==no):
           value+=1
           break;

    if(value>=1):
       print("number is present") 
    else:
       print("number is not present") 




check(list,num)
