# pass by value : 

def change(n):
    n+=10
    print(f'inside:{n}')
n=10.2
change(n)
print(f'outside:{n}')

# pass by reference :
def changelist(l):
    l.append(50)
    print(f'inside:{l}')
lst=[10,20,30,40]
changelist(lst)
print(f'outside:{lst}')

# mutable : list , dict , set
# immutable : int , float , str , tuple

# pass by object reference :
def changevalue(x):
    x+=5
    print(f'inside:{x}')
a=15
changevalue(a)
print(f'outside:{a}')
def changearray(arr):
    arr[0]=99
    print(f'inside:{arr}')
array=[1,2,3,4,5]
changearray(array)
print(f'outside:{array}')