def run():
    y = "yY"
    n = "nN"
    def again():
        select = input("a. add, b. subtract, c. multiply, d.divide : ")
        if select == "a":
            number1 = input("Enter First Number: ")
            number2 = input("Enter Second Number: ")
            result = int(number1) + int(number2)
            print("Result: ", result)
            q = input("Y/y or N/n : ")
            if q in y:
                run()
            if q in n:
                print("Thank You! Bye!")
        if select == "b":
            number1 = input("Enter First Number: ")
            number2 = input("Enter Second Number: ")
            result = int(number1) - int(number2)
            print("Result: ", result)
            q = input("Y/y or N/n : ")
            if q in y:
                run()
            if q in n:
                print("Thank You! Bye!")
        if select == "c":
            number1 = input("Enter First Number: ")
            number2 = input("Enter Second Number: ")
            result = int(number1) * int(number2)
            print("Result: ", result)
            q = input("Y/y or N/n : ")
            if q in y:
                run()
            if q in n:
                print("Thank You! Bye!")
        if select == "d":
            number1 = input("Enter First Number: ")
            number2 = input("Enter Second Number: ")
            result = 0 if int(number2) == 0 else (int(number1) / int(number2))
            print("Result: ", result)
            q = input("Y/y or N/n : ")
            if q in y:
                run()
            if q in n:
                print("Thank You! Bye!")
    again()
run()
