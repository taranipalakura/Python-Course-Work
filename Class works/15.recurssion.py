# print 1 to 10 using recursion :

def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
display(1)

# print 6 to 1 using recursion :
 
def display(n):
    if n==6:
        return
    display(n+1)
    print(n)
display(1)

# print string using recursion :

def display(s,ind):
    if ind==len(s):
        return
    print(s[ind])
    display(s,ind+1)
s="subhash"
display(s,0)

# string is A,B,C first print abcdef then print a down ab down abc and abcdef down abcde down abcdef is the last one : 

def dispaly(ind):
    if ind==len(s):
        return
    print((s[:ind+1]))
    dispaly(ind+1)
s="subhash"
dispaly(0)

# 
def display(ind,w):
    if ind==len(s)-w+1:
        return
    print((s[ind:ind+w]))
    display(ind+1,w)
s="subhash"
display(0,3)
