# Square Number Ask the user for a number and print its square (the product of the number times itself).

# Here's a sample run of the program (user input is in bold italics):

# Type a number to see its square: 4

Square_Number = float(input("Type a number to see its square: "))
# 1st method
new_Square= pow(Square_Number,2) 
print(f'{ Square_Number} squared is {new_Square}')
print("2nd method \U0001F447")
# 2nd method 👇
new1_Square= Square_Number  * Square_Number

print(f'{ Square_Number} squared is {new1_Square}')