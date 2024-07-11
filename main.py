from Shop import Shop

myShop = Shop("Music Reverb", 0)

print(f"welcome to {myShop.name} !!")
choose = input("📑 To display the product catalog press 1\n"
               "➕ To add a second-hand product, press 2\n"
               "🛒 To buy product press 3\n"
               "🔚 To turn off write off\n")

while choose != "off":
    if choose == '1':
        myShop.print_catalog()
    elif choose == '2':
        myShop.add_second_hand_product()
    elif choose == '3':
        myShop.buy()
    choose = input("📑 To display the product catalog press 1\n"
                   "➕ To add a second-hand product, press 2\n"
                   "🛒 To buy product press 3\n"
                   "🔚 To turn off write off\n")
print("by,by!!")
