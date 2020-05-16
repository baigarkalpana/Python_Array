'''
Author:Kalpana Baigar
Program to print the list
'''

list=[]

def accept(lst):
    for x in range(0,5):
        lst.append(x)

    
def display(lst):
    for x in lst:
        print(x,end=' ')


accept(list)

display(list)
