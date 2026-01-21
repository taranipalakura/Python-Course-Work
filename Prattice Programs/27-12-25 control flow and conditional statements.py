# Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
a,b,c,= tuple(map(int,input().split()))
if a==b and b==c:
    print("Eq")
elif a!=b and b!=c and a!=c:
    print("sc")
else:
    print("Is")
    
# Electricity bill calculator based on units used :

units = int(input())
bill=0
if 0<=units<=100:
    bill=units
elif 100< units<=200:
    bill=100+(units-100)*2
elif units>200:
    bill=300+(units-200)*3
print(bill)

# Amstrong number : 
num =input()
sum=0
l=len(num)
for i in num :
    sum+=int(i)**l
if sum==int(num):
    print("Arm")
else:
    print("not Arm")
    
    # or #
num=int(input())
temp=num
sum=0
l=len(str(num))
while num>0:
    sum+=(num%10)**l
    num//=10
if sum==temp:
    print("Arm")
else:
    print("not Arm")
    
# Validate strong password (min 8 chars, 1 uppercase, 1 digit, 1 special char)

pwd=input()
if len(pwd)>=8:
    s=set()
    for i in pwd:
        if i.isupper():
            s.add('u')
        elif i.islower():
            s.add('l')
        elif i.isdigit():
            s.add('d')
        else:
            s.add('s')
    if len(s)==4:
        print("strong password")
    else:
        print("weak password")
else:
    print("weak password,length needs to be >=8")
    
# Ticket fare calculator with age-based discounts:

age=int(input())
fee=0
if 0<=age<5:
    pass
elif 5<=age<18:
    fees=100-100*(0.5)
elif age >60:
    fees=-100- 100*0.3
else:
    fees=100
print(fees)

# 24-hour to 12-hour time converter:

hrs,mins=tuple(map(int,input().split(':')))
if 0<=hrs<12 and 0<=mins<=59:
    print("f:{hrs}:{mins}AM")
elif hrs==12:
    print(f"{hrs}:{mins}PM")
else:
    print(f'{hrs-12}:{mins}PM')
    
# currency denomination 

n = [2000,500,100,50,10]
amount = int(input("Enter amount: "))
for i in n:
    if amount >= i:
        t = amount//i
        amount %= i
        print(f'{t} *{i}')
        
# Find the largest of three numbers:
a,b,c=tuple(map(int,input().split()))
if a>=b and a>=c:
    print(a)
elif b>=a and b>=c:
    print(b)
else:
    print(c)

# Check if a number is prime or not:
num=int(input())
if num>1:
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")
    
# Check if a year is a leap year or not:
year=int(input())
if (year%4==0 and year%100!=0) or (year%400
==0):
    print("leap year")
else:
    print("not leap year")
    
# Calculate the factorial of a number:
num=int(input())
fact=1
for i in range(1,num+1):
    fact*=i
print(fact)

# Generate Fibonacci series up to n terms:  
n=int(input())
a,b=0,1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()

# Check if a number is even or odd:
num=int(input())
if num%2==0:
    print("even")
else:
    print("odd")
    