while True:

    print("\n" + "=" * 40)
    print("        PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print("=" * 40)

    choice = int(input("Enter your choice: "))

    if choice == 1:
        first = int(input("Enter 1st Number: "))
        second = int(input("Enter 2nd Number: "))

        result = first + second

        print("\n----------------------------")
        print("Addition Successful")
        print("Answer:", result)
        print("----------------------------")

    elif choice == 2:
        first = int(input("Enter 1st Number: "))
        second = int(input("Enter 2nd Number: "))

        result = first - second

        print("\n----------------------------")
        print("Subtraction Successful")
        print("Answer:", result)
        print("----------------------------")

    elif choice == 3:
        first = int(input("Enter 1st Number: "))
        second = int(input("Enter 2nd Number: "))

        result = first * second

        print("\n----------------------------")
        print("Multiplication Successful")
        print("Answer:", result)
        print("----------------------------")

    elif choice == 4:
        first = int(input("Enter 1st Number: "))
        second = int(input("Enter 2nd Number: "))

        if second != 0:
            result = first / second

            print("\n----------------------------")
            print("Division Successful")
            print("Answer:", result)
            print("----------------------------")

        else:
            print("\n----------------------------")
            print("Cannot Divide By Zero")
            print("----------------------------")

    elif choice == 5:
        print("\n================================")
        print("    Thank You For Using")
        print("     PYTHON CALCULATOR")
        print("================================")
        break

    else:
        print("\n----------------------------")
        print("Invalid Choice")
        print("Please Enter A Number Between 1 And 5")
        print("----------------------------")
