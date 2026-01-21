# Exception Handling in Python
# Exception handling is a mechanism to handle runtime errors, allowing the program to continue its execution instead of crashing.
# In Python, exceptions can be handled using the try, except, else, and finally blocks.
# The try block contains the code that may raise an exception.
# The except block contains the code that runs if an exception occurs.
# The else block runs if no exceptions occur in the try block.
# The finally block runs regardless of whether an exception occurred or not, typically used for cleanup actions.

# 1. By using try, except, and finally to handle division by zero and invalid input.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    result = a / b
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

except ValueError:
    print("Error: Please enter valid integers")

finally:
    print("Program execution completed")

# 2.Here is an example demonstrating various exception handling scenarios :

try:
    a=10
    b=a/0
except ZeroDivisionError:
    print("You can't divide number with zero")
except NameError:
    print("Value is not defined")
except KeyError:
    print("Key is not present in dict")
except IndexError:
    print("Index is not present in the seq")
except ValueError:
    print("Enter the proper value")
except TypeError:
    print("data Type is different ")
else:
    print("Code Success, No Error")
finally:
    print("End of Try block")
print("Rest of the code")

# 3.insteade of multiple except blocks we can use single except block to handle all exceptions :

try:
    a={1:1,2:4,3:9}
    b=a[4]

except (ZeroDivisionError,NameError,KeyError,IndexError,ValueError,TypeError) as e:
    print(f"Error Occured: {e}")
else:
    print("Code Success, No Error")
finally:
    print("End of Try block")
print("Rest of the code")

# 4. Using a single except block to catch all exceptions:

try:
    a=10
    b=a/c

except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Code Success, No Error")
finally:
    print("End of Try block")
print("Rest of the code")

# 5. Raising a custom exception:

try:
    a=-1000
    if a<0:
        raise Exception("You can't withdraw -ve amount")
except Exception as e:
    print(f"Error Occured: {e}")
else:
    print("Transaction Success")
finally:
    print("End of Transaction")
    