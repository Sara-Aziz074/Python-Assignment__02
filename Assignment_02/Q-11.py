# Get a List Write a program which continuously asks the user to enter values which are added one by one into a list. When the user presses enter without typing anything, print the list.

# Initialize an empty list
my_list = []

while True:
    # Get user input
    user_input = input("Enter a value: ")
    
    # Check if the input is empty
    if user_input == "":
        # Print the list and exit the loop
        print("Here's the list:", my_list)
        break
    
    # Add the input to the list
    my_list.append(user_input)