# # Write your AC Load Estimator solution here
# Get the input from the user.
# You'll need to ask for:

# width of the room
width = float(input("Enter the width of the room in m: "))

# height of the room
height = float(input("Enter the height of the room in m: "))

# number_of_people in the room
number_of_people = int(input("Enter the number of people in the room: "))

# Calculate the horsepower using the formula
horsepower = width * height * 0.1 + number_of_people * 0.06

# Print out the horsepower.
print(horsepower)

# Run the tests to check your answer.
