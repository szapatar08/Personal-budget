import functions

expences = []

while True:
    try:
        system = int(input("1 - Add income\n2 - Add expence\n3 - Exit\nWhat do you want to do? "))
        if system < 1 or system > 3:
            print("Enter a valid value\n")
        else:
            if system == 1:
                print("")
            elif system == 2:
                print("")
            else:
                break
    except:
        print("Enter a valid value\n")