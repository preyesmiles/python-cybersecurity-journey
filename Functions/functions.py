# Create a program that can take in input of the users name
# save the name in a variable
# pass the variable through a function and print "Hello _______”

# Takes an input of the the users name
name = input("What is your name? ")

# Defines the function and what it should do
def display(name):
    print(f"Hello {name}")

# Calls the function
display(name)