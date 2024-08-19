# Write a program that reads three edges for a
# triangle and computes the perimeter if the input is valid. Otherwise, display that
# the input is invalid. The input is valid if the sum of every pair of two edges is
# greater than the remaining edge. 

#declare your varibles side_a ,side_b,side_c,perimeter
#declare a prompt that ask the user for the sides of the triangle seperated by a comma
#extract the variales
#convert the variables from string type to integer type to be able to perform arithmetic operation
#
#check if input is valid 
#display result



edges = eval(input("Enter the lengths of the three edges separated by commas: "))

# Unpack the edges into a, b, and c
a, b, c = float(edges[0]), float(edges[1]), float(edges[2])

# Check if the input is valid
if (a + b > c) and (a + c > b) and (b + c > a):
    # Compute the perimeter
    perimeter = a + b + c
    print("The perimeter of the triangle is:", perimeter)
else:
    print("The input is invalid. The sum of any two edges must be greater than the remaining edge.")
    