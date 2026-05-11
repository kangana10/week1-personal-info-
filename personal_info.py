# Name: Kangana Batghare
# Project: Personal Information Program

# Welcome message
print("╔══════════════════════════════╗")
print("     Welcome to My Program!")
print("╚══════════════════════════════╝\n")

# -------------------------------
# Static Personal Information
# -------------------------------

# Storing name as a string
name = "Kangana"

# Storing age as an integer
age = 18

# Storing city as a string
city = "Bhilai"

# Storing hobby as a string
hobby = "Singing"

# Calculating age in months
age_in_months = age * 12

# -------------------------------
# Taking User Input
# -------------------------------

print("We would love to know some of your favourite things! :D")

# Asking user for favorite food
favorite_food = input("Enter your favorite food: ").strip() #strip() is used to remove any leading or trailing whitespace from the input

# Validation for favorite food
while favorite_food == "":
    print("Favorite food cannot be empty!")
    favorite_food = input("Please enter your favorite food: ").strip()

# Asking user for favorite color
favorite_color = input("Enter your favorite color: ").strip()

# Validation for favorite color
while favorite_color == "":
    print("Favorite color cannot be empty!")
    favorite_color = input("Please enter your favorite color: ").strip()

# -------------------------------
# Formatting Strings
# -------------------------------

# Using string methods to format output
favorite_food = favorite_food.title() 
#title() will capitalize the first letter of each word in the string

favorite_color = favorite_color.capitalize()
#capitalize() will capitalize the first letter of the string and make the rest of the letters lowercase 

name = name.title()
city = city.title()
hobby = hobby.capitalize()

# -------------------------------
# Displaying Information
# -------------------------------

print("\n" + "." * 40)
print("   PERSONAL INFORMATION OF THE USER    ")
print("." * 40)

print(f"Name           : {name}")
print(f"Age            : {age} years")
print(f"Age in Months  : {age_in_months} months")
print(f"City           : {city}")
print(f"Hobby          : {hobby}")

print("\n" + "-" * 40)

print("      USER FAVORITES")
print("-" * 40)

print(f"Favorite Food  : {favorite_food}")
print(f"Favorite Color : {favorite_color}")

print("=" * 40)

# Goodbye message
print(f"\nThank you for using the program, {name}!")
print("Have a great day ahead! goodbyeee!")