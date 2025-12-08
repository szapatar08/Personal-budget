class menus:
    def income_menu():
        while True:
            try:
                system = int(input("1 - Add income\n2 - Show incomes\n3 - Change the value\n4 - Remove incomes\n5 - Quit\nWhat do you want to do?"))
                if system < 1 or system > 5:
                    print("Enter a valid value\n")
                else:
                    if system == 1:
                        print("")
                    elif system == 2:
                        print("")
                    elif system == 3:
                        print("")
                    elif system == 4:
                        print("")
                    else:
                        break
            except:
                print("Enter a valid value\n")