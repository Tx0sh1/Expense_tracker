# Print welcome message for the expense tracker
print("Welcome to the expense tracker")
print("")

# Dictionary to hold categories of expenses and their initial values (set to 0)
expense = {
    'food': 0,
    'rent': 0,
    'transport': 0,
    'Life Policies': 0,
    'maintenance': 0
}

# Extracting keys (categories) from the expense dictionary into a list
cat = list(expense.keys())

# Start of the main program loop
while True:
    # Ask the user whether they want to add expenses or exit
    c = input("press y to add expenses or n to exit \n")
    
    if c == "y":  # If the user chooses to add expenses
        # Create an empty dictionary to store entered amounts for each category
        amounts = {}

        # Loop through each category in the list `cat`
        for i in cat:
            while True:  # Loop to handle input validation
                try:
                    # Prompt user to enter the amount for the current category
                    x = int(input(f"Enter amount for {i}: "))
                    amounts[i] = x  # Add the entered amount to the `amounts` dictionary
                    break  # Exit the loop if input is valid
                except ValueError:  # Handle invalid input
                    print("enter an amount in numbers!")
        
        # Create lists of keys (categories) and values (amounts) from the `amounts` dictionary
        k_list = list(amounts.keys())
        v_list = list(amounts.values())
        
        # Calculate the total of all expenses
        total = sum(amounts.values())

        # Loop through the lists of categories and amounts to print details
        for k, v in zip(k_list, v_list):
            print(f"You've entered R{v} for {k}")
        
        # Print the total expenses
        print(f"Your total comes up to R{total}")

    elif c == "n":  # If the user chooses to exit
        # Print goodbye message and break the loop
        print("Goodbye!")
        break
