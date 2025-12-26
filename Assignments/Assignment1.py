# Fitness Tracking System Using Different Data Types and Formatting Methods
# This program collects fitness-related data from the user
# and displays it using various Python data types and formatting techniques.

# -------------------------------
# Task 1: Take Fitness Details as Input
# -------------------------------

# Taking user ID as an integer
user_id = int(input("Enter User ID: "))

# Taking user name as a string
user_name = input("Enter User Name: ")

# Taking weight as a floating-point value
weight = float(input("Enter Weight: "))

# Taking multiple workout types as a comma-separated string
# and converting it into a list
workout_types = input("Enter Workout Types: ").split(",")

# Taking step target and steps completed as integers
step_target = int(input("Enter Step Target: "))
steps_completed = int(input("Enter Steps Completed: "))

# Storing step data as a tuple (immutable data type)
daily_steps = (step_target, steps_completed)

# Taking calories burned as a float
calories_burned = float(input("Enter Calories Burned: "))

# Taking fitness goals as comma-separated values
# and converting them into a set to store unique goals
fitness_goals = set(input("Enter Fitness Goals: ").split(","))

# Taking trainer details as strings
trainer_name = input("Enter Trainer Name: ")
trainer_contact = input("Enter Trainer Contact Number: ")
gym_location = input("Enter Gym Location: ")

# Storing trainer details in a dictionary (key-value pairs)
trainer_details = {
    "name": trainer_name,
    "contact": trainer_contact,
    "location": gym_location
}

# -------------------------------
# Task 2: Display Fitness Details Using Different Formatting Methods
# -------------------------------

# 1. Using Comma Separation (sep=',')
# This prints values separated by commas
print("\nUsing Comma Separation (sep=',')")
print("User ID", "Name", "Weight", sep=", ")
print(user_id, user_name, weight, sep=", ")

# 2. Using Percentage Formatting (% operator)
# Calculating percentage of steps completed
step_completion_percentage = (steps_completed / step_target) * 100

# Printing percentage using % formatting
print("\nUsing Percentage Formatting")
print("Steps Completion: %.2f%%" % step_completion_percentage)

# 3. Using f-strings
# Displaying fitness details using f-string formatting
print("\nUsing f-strings")
print(f"User Name: {user_name}")
print(f"Weight: {weight} kg")
print(f"Calories Burned: {calories_burned} kcal")
print(f"Steps Completed: {steps_completed}/{step_target}")

# 4. Using .format() method
# Displaying trainer details using .format() method
print("\nUsing .format() method")
print("Trainer Details: Name - {}, Contact - {}, Location - {}".format(
    trainer_details["name"],
    trainer_details["contact"],
    trainer_details["location"]
))
