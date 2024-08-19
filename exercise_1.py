# Write a program that prompts the user to enter a
# point (x, y) and checks whether the point is within the circle centered at (0, 0) with
# radius 10. For example, (4, 5) is inside the circle and (9, 9) is outside the circle, as
# shown in Figure 4.8a

#declare a variable that stores the value of x and y
#display a prompt that ask the user for input x and y
#convert the user input from string type to integer type
#check if the value of x and y is inside or outside the circle
#Display the result
import math

# Prompt the user to enter the coordinates of the point
x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# Calculate the distance from the point to the center (0, 0)
distance = math.sqrt(x * x + y * y)

# Check if the distance is less than or equal to 10
if distance <= 10:
    print("The point is inside the circle.")
else:
    print("The point is outside the circle.")