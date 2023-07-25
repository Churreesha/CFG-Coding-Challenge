#Hide Credit Card Digits in Python
#First, we import the random module, which provides us with functions to generate random numbers.
# Import the random module
import random

# Define a function to generate a random credit card number
#define a function called generate_card(), which takes no parameters and returns a random credit card number as a string
def generate_card():
    # Initialize an empty string to store the number
    number = ""
    # Loop 4 times
    for i in range(4):
        # Generate a random 4-digit number and convert it to a string
        digits = str(random.randint(1000, 9999))
        # Append the digits and a space to the number string
        number = number + digits + " "
    # Return the number string without the trailing space
    return number.strip()

# Define a function to hide the first 12 digits of a credit card number
def hide_card(number):
    # Split the number string by spaces and store it in a list
    parts = number.split()
    # Loop through the first 3 elements of the list
    for i in range(3):
        # Replace each element with "XXXX"
        parts[i] = "XXXX"
    # Join the list elements with spaces and return the result
    return " ".join(parts)

# Test the functions with an example
card = generate_card()
print(card) # For example: 5486 3251 6584 7855
hidden = hide_card(card)
print(hidden) 

