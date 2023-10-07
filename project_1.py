# Get the user's name
name = input("What's your name? ")

# Get the user's age
age = int(input("How old are you? "))

# Greet the user
print(f"Hi, {name}!")

# Provide a personalized message based on age
if age < 18:
    print("You are quite young!")
elif age >= 18 and age < 30:
    print("You are in your prime!")
else:
    print("You have a lot of life experience!")

# Additional message
print("Thank you for using this program.")
