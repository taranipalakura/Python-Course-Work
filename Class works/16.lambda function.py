# functions with no name and which have a single expression are called lambda functions.
# They're "disposable" functions.
# To build stateful, multi-step workflows that can run for up to one year.

# normal function to welcome a user and lambda function to do the same task :

def wish(name):
    return f"welcome to python course {name}!!"
wish1=lambda name:f"welcome to python course {name}!!"
print(wish("lakshmi venkata sai"))
print(wish1("subhash"))
 
# greatest of two numbers using normal function and lambda function :

greatest=lambda a,b,c: a if (a>b and a>c) else (b if (b>c) else c)
print(greatest(19,12,15))

# sum of three numbers using normal function and lambda function :

def sum(a,b,c):
    return a+b+c
sum1=lambda a,b,c:a+b+c
print(sum1(19,12,12))
print(sum1(15,20,23))

# Addition of two numbers :

a=lambda x,y:x+y
print(a(3,6))

# square of numbers in a list using lambda function and map function :

lst=[1,2,3,4,5,6,7,8,9,10]
def square(l):
    for i in range(len(l)):
        l[i]=l[i]**2
        return l
n=list(map(lambda x:x**2,lst))
print(n)

# or # with lambda function : 

def evennumbers(l):
    res=[]
    for i in l:
        if i%2==0:
            res.append(i)
    return res

# with out lambda function :
l=[1,2,3,4,5,6,7,8,9,10]
n=list(filter(lambda i:i%2==0,l))
print(evennumbers(l),n)

# with lambda function :
def filtervol(s):
    res=[]
    for i in s:
        if i in vol:
            res.append(i)
    return res

# without lambda function :
s="subhash"
vol="aeiou"
n=list(filter(lambda i:i in vol,s))
print(filtervol(s),n)

# removes 0:(with lambda function) :

def removezeros(l):
    res=[]
    for i in l:
        if i!=0:
            res.append(i)
    return res

# with out lambda function :
l=[0,2,3,0,4,5,0,6,7,0]
n=list(filter(lambda i:i!=0,l))
print(n,removezeros(l))

# 1.map()-it applies a function to all the items in an input list.

x = [10, 20, 31, 42, 51]
y = list(map(lambda x: x * 2, x))
print(y)

# filter()-it creates a list of elements for which a function returns true.
x = [20,31,10,42,51]
y = list(filter(lambda x: x % 2!=0,x))
print(y)

# reduce()-it applies a rolling computation to sequential pairs of values in a list.
from functools import reduce
x = [10, 20, 32, 42, 51]
y = reduce(lambda x, y: x + y, x)
print(y)
