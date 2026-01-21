# Generator functions in Python are a simple and powerful tool for creating iterators.
# They allow you to declare a function that behaves like an iterator, i.e., it can be used in a for loop.
# Generators are written like regular functions but use the yield statement whenever they want to return data.
# Each time next() is called on it, the generator resumes where it left off (it remembers all the data values and which statement was last executed).

def reels():
    data= ['1..100','101..200','201..300','301..400']
    for i in data:
        yield i

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))

# 

def reels():
    yield "First Reel"
    yield "Second Reel"
    yield "3s"
    yield "4s"
    yield "5s"

scroll = reels()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))