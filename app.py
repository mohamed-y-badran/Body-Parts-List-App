x = "random"
bod = []

def show_menu():
    print('Menu')
    print ("1. Add a body part")
    print ("2. Remove a body part")
    print ("3. Go to Items")
    print ("4. Exit")

while x != "4":

    show_menu()
    x = input('HI! Enter Choice 1-4')
    
    if x == '1':
        item = input("Add a body part: ")
        bod.append(item)
        print('Item Added', item)
        
    elif x == '2':
        item = input("what is to be removed ??")
        if item in bod:
            bod.remove(item)
            print('Item removed', item )
        else:
            print("Item Doesn't exist")

    elif x == "3":
        print('List of Body Parts:')
        for item in bod:
            print(item)

    elif x == '4':
        print('Good Bye')
    else:
        print('Enter Valid Value 1-4')