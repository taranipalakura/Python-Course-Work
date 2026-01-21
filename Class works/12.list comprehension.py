# List comprehension : short and clean way to create lists using a single line of code instead of long for loops.

even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

result = ["Even" if x % 2 == 0 else "Odd" for x in range(1, 6)]
print(result)

lc=[i for i in range(1,11)]
print(lc)

resl=[i for i in range(1,11) if i%2==0]
print(resl)

namesl=[input("enter the names:") for i in range(5)]
print(namesl)

s='python programming'
v='aeiouAEIOU'
r=[i if i in v else 0 for i in s]
print(r)

# set Comprehension: 

s='python programming language'
r=(i for i in s)
print(r)

# Tuple :

s='python programming language'
r=tuple(i for i in s)
print(r)

# dictionary :

d1={i:i*i for i in range(1,6)}
print(d1)

d1={input("enter the product:"): input("enter the price:") for i in range(1,6)}
print(d1) 