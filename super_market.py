def super_market(product,price,qun):
    print(f"'product, 'price' 'quantity'")
    for i in range(len(product)):

        print(f"{product[i]}    {price[i]}  {qun[i]}")
def update_price(item,product,price):
    if item in product:
        index = product.index(item)
        price[index] = int(input("Enter price of product:"))
    else:
        print("Product is not found")
def update_qun(item,product,qun):
    if item in product:
        index = product.index(item)
        qun[index] = int(input("Enter a quantity of a product:"))

    else:
        print("Product is not found")




product = ["milk","sugar","rice","drinks","eggs"]
price = [50,45,55,20,6]
qun = [5,10,20,25,150]


flag = True
while(flag):
    print("Enter super market")
    choose = input("enter yes or no:")
    if choose=='yes':
        print("choose choice:\n1.print all items in the market\n2.update price of a product\n3.update quantity of a product")
        choice = int(input("Enter choice:"))
        if choice==1:
            super_market(product,price,qun)
        elif choice==2:
            item = input("Enter a product name:")
            update_price(item,product,price)
        elif choice==3:
            item = input("Enter a product name:")
            update_qun(item,product,qun)
        else:
            print("enter choice in b\w 1 to 3")
    elif choose=='no':
        flag = False
    else:
        print("You have entered wrong input:")
