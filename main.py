print("Welcome to the expense tracker")

expense = {
    'food': 0,
    'rent': 0,
    'transport': 0,
    'Life Policies' : 0,
    'maintainance ' : 0
}

while True:
    c = input(" press y to add expenses or n to exit \n ")
    if c == "y":
        try:
            expense['food'] = int(input("enter the amount u use on food: \n"))
            expense['rent'] = int(input("enter the amount you use on rent: \n"))
            expense['transport'] = int(input("enter the amount you use on transport: \n"))
            expense['Life Policies'] = int(input("enter the amount you use on life policies: \n"))
            expense['maintainance '] = int(input("enter the amount you use for maintainance : \n"))
            
            total = expense['food'] + expense['rent'] + expense['transport'] + expense['Life Policies'] + expense['maintainance ']

            print(f"you entered R{expense['food']} for food, R{expense['rent']} for rent, \
                R{expense['transport']} for transport, R{expense['Life Policies']} for life policies, \
                and R{expense['maintainance ']} for maintainance , which makes a total of R{total}")
            
        except ValueError:
            print("enter an amount in numbers!")
    if c == "n":
        ("Print Goodbye")
        break
