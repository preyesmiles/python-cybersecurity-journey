# This program accepts an input "score", evaluates the input and prints out the grade that corresponds to the number inputed.

# This code section accepts input and assigns it to the variable score as an integer data type.
score = int(input("Enter your score: "))

# This code sections evaluates input using the if statement and conditional operators to determine garde.
# It also includes nested if statements and shows how it works.
if score >= 90 and score <= 100:
    age = int(input("Enter your age: "))
    if age < 10:
     print("Grade A+")
    else:
     print("Grade A")
elif score >= 80 and score <= 89:
      age = int(input("Enter your age: "))
      if age < 10:
         print("Grade B+")
      else:
         print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
elif score < 60:
    print("Grade F")
else:
    print("invalid Grade")