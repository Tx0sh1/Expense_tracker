print("Welcome to the expense tracker")
print("")

expense = {
    'food': 0,
    'rent': 0,
    'transport': 0,
    'Life Policies' : 0,
    'maintenance' : 0
}

cat = list(expense.keys())

while True:
    c = input("press y to add expenses or n to exit \n")
    if c == "y":
        
            
            amounts = {}  # Dictionary to store amounts for each category

            for i in cat:
                while True:
                    try:
                        x = int(input(f"Enter amount for {i}: "))
                        amounts[i] = x  # Store the input amount with the category as the key
                        break
                    except ValueError:
                        print("enter an amount in numbers!")
            
            k_list = list(amounts.keys())
            v_list = list(amounts.values())        
            total =sum(amounts.values())

            for k, v in zip(k_list, v_list):
                print(f"You've entered R{v} for {k}")
            print(f"Your total comes up to R{total}")
            
                
    elif c == "n":
        print("Goodbye!")
        break
    