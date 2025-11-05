name = input("Enter your name: ")
height = float(input("Enter your height: ")) #Convert to float

#Input Validation
while True:
    try:
        age = int(input("Enter your age: "))
        if age > 0:
            break
        else:
            print("Age must be positive!")
    except ValueError:
        print("Please enter a valid number!")

#Output Validation
print(f"Hello, {name}!")
print(f"You are {age} years old and {height} feet tall.")

#Exercise 1 Create a simple calculator that takes two number and an operation from user.
num1 = float(input("Enter first number:"))

#Exercise 2 Create a simple quiz program with 3 questions. At the end of the quiz, display score.