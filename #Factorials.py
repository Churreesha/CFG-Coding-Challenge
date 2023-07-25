#Factorials
# Define a function to find the factorial of n using a lookup table
def factorial(n):
    # Initialize an empty dictionary to store the factorials
    lookup = {}
    # If n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # If n is in the lookup table, return its value
    if n in lookup:
        return lookup[n]
    # Otherwise, calculate the factorial recursively and store it in the lookup table
    else:
        lookup[n] = n * factorial(n - 1)
        return lookup[n]

# Test the function with some examples
print(factorial(1)) 
print(factorial(2)) 
print(factorial(3)) 
print(factorial(4)) 