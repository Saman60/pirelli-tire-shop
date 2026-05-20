def current_stock():
    print(f"The shop has {stock} tyres.")

def stocking():
    amount = int(input("Enter how many tyres u're Stocking: "))
    if amount <= 0:
        print("please buy some tyres")
        return 0
    else:
        return amount

def selling():
    amount = int(input("How many tires u wanna buy: "))
    if amount > stock:
        print("Insufficient stock.")
        return 0
    elif amount < 0:
        print("please enter greater then 0.")
        return 0
    else:
        return amount

stock = 0
is_running = True

while is_running:
    print("\nWelcome to Pirelle Tire Shop!!")
    print("1.See the current num of tires")
    print("2.Stock up the shop.")
    print("3.Buy some Tires.")
    print("4.Exit the shop.")

    choice = input("Enter your choice 1 to 4: ")
    if choice == '1':
        current_stock()
    elif choice == '2':
        stock += stocking()
    elif choice == '3':
        stock -= selling()
    elif choice == '4':
        is_running = False
    else:
        print("That isnt valid choice.")

print("Thanks for visiting!!")