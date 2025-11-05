#if-else: 2 conditions
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

#if-elif-else: more than 2 conditions
score = 40

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# and: both conditions mist be True
user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You are allowed to drive")
else:
    print("You are not allowed to drive")

# or: at least one condition must be True
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday")

# Nested conditions: Condition within condition
weather = "sunny"
temp = 75

if weather == "sunny":
    if temp > 70:
        print("It's sunny and warm.")
    else:
        print("It's sunny but cool")


# Exercise: Write a program that categorizes BMI (Body Mass Index) into underweight(<18.5), normal weight(<24.9), overweight(<29.9), and obesity(>30.0). (formula = kg/m^2)
weight = 100

if weight <= 18.5