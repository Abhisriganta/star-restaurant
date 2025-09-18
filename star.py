menu={
    'pizza':150,
    'pasta':80,
    'burger':200,
    'salad':100,
    'coffee':50,

}

print("Welcome to Star Restaurant")
print("pizzza: Rs150\n pasta:Rs80\n,burger:Rs200\n,salad:Rs100\n, coffee:Rs50")

order_total = 0
 
item_1 = input("Enter name of the item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print("Your item {{item_1}} has been added to your order")

else:
    print("Please order item {item_1} is not available yet1")
another_order = input("Do you want to add another item? (yes/no)")
if another_order == "yes":
    item_2 = input("Enter the second item name=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {{item_2}} has been added to your order")
    else:
        print(f"Ordered item is not available!")
print(f"The total amount of items to pay is {order_total}")



