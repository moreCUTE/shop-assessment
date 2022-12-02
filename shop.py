inventory = ["empty", "empty", "empty"]
mulah = 50

def shop(x):
    doExit = False
    while doExit is False:
        print("Welcome to my shop")
        print("you have", x, "coins.")
        print("Inventory: ", inventory)
        print("items for sale: yoyo for 5 coins, dr.thunder for 3 coins, and lockpick for 10 coins")
        print("press y for yoyo, d for dr.thunder, and l for lockpick")
        print("press q to quit")
        choice = input()
        if choice == 'y':
            if x >= 5:
                print("You got a yoyo")
                inventory[0] = "yoyo"
                x -= 5
            else:
                print("you dont have enough coins for that go mow a lawn")
            print("------------")
        elif choice == 'd':
            if x >= 3:
                print("you got the legendary DR.THUNDER")
                inventory[1] = "dr.thunder"
                x -= 3
            else:
                print("you lowk broke rn go shovel some snow")
            print("------------")
        elif choice == 'l':
            if x >= 10:
                print("you have aquired a lockpick")
                inventory[2] = "lockpick"
                x -= 10
            else:
                print("you cant afford this item, go make a lemonade stand foo")
            print("------------")
        elif choice == 'q':
            print("Goodbye")
            print("------------")
            doExit = True
        else:
            print("we dont sell that...")
            print("ur dum")
            print("------------")
    
room = 1
print("You are in room 1")

if room == 1:
    shop(mulah)
            

