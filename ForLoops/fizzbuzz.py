# Fizzbuzz
# in a range of numbers from 1 to 100
# If a number is divisible by 3, print fizz
# If a number is divisible by 5, print buzz
# If a number is divisible by both, print fizzbuzz

# Option1
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# Option2
for i in range(1, 101):
    output = ""

    if i % 3 == 0:
        output += "Fizz"

    if i % 5 == 0:
        output += "Buzz"

    if output == "":
        print(i)
    else:
        print(output)

# Option3
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    print(output or i, end=", ")