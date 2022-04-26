print()
print(f"Welcome to the Shoping Cart Program!")
menu_selection = 0

shopping_cart = []
prices = []

while(menu_selection != 5):
    print("1. Add Item")
    print("2. View Cart")
    print("3. Remove Item")
    print("4. Compute Total")
    print("5. Quit")

    menu_selection = int(input("Please Enter An Action: "))
    if menu_selection < 1 or menu_selection > 5:
        print("Invalid Choice!")

    if menu_selection == 1:
        item = input("What item would you like to add? ")
        shopping_cart.append(item)
        price = float(input(f"What is the price of {item}? "))
        prices.append(price)
        print(f"{item} for ${price} has been added to the cart")

    elif menu_selection == 2:
        print()
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            print(f"{i+1}. {shopping_cart[i]} - ${prices[i]}")
        print()
#remove item
    elif menu_selection == 3:
        item = int(input("What item would you like to remove? "))
        item -= 1

        if item < 0 or item > len(prices):
            print("Invalid selection, item not in list")

        else:
            thing = shopping_cart[item]
            shopping_cart.pop(item)
            prices.pop(item)

    elif menu_selection == 4:

        sum = 0
        for price in prices:
            sum += price
            
        print("*" * 20)
        print(f"The total price of the items in the shopping cart is ${sum: .2f}")
        print("*" * 20)
    
    elif menu_selection == 5:
        print("Thank you and goodbye!")