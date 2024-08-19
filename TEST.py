# Suppose you shop for rice and find it in two differentsized packages. You would like to write a program to compare the costs of the
# packages. The program prompts the user to enter the weight and price of each
# package and then displays the one with the better price

#solution
# declare two variables for each package,variable_one ,variable_two
#display a prompt,
# wait fo the user input
#Store the user input in the corresponding variable


weight_1, price_1 = eval(input("Enter the weight and price of package 1 seperated by comma: "))

weight_2, price_2 = eval(input("Enter the weight and price of package 2 seperated by comma: "))
# this code line modified the question for checking both weight and price
if weight_1 > weight_2:
    if price_1 > price_2:
        print("package 1 has the better price.")
    else:
        print("price 2 is greater than price 1")
else:
    if price_1 > price_2:
        print("package 1 has the better price.")
    else:
        print("price 2 is greater than price 1")



