import sys
func = ""
def login():
    user_name = input("Enter your username >")
    password = input("Enter your password >")
    if user_name=="paul" and password=="1234":
        operation()
    else:
        login()

def operation():
    global func
    print("""Enter your operation:
            1. addition
            2. subtraction
            3. division
            4. quit""")
    option = input(">>> ")
    if option=="1":
        func = "addition"
        addition()
    elif option=="2":
        func = "subtract"
        subtract()
    elif option=="3":
        func = "division"
        division()
    elif option=="4":
        sys.exit()
    else:
        print("Invalid input")
        operation()

def tryAgain():
    print("Enter 1. perform operation again, 2. go to menu")
    user = input(">>>")
    if user=="1":
        if func=="addition":
            addition()
        elif func=="subtract":
            subtract()
        elif func=="division":
            division()
    elif user=="2":
        operation()
    else:
        print("Invalid input")
        tryAgain()

def subtract():
    val1 = int(input("Enter value 1 >"))
    val2 = int(input("Enter value 2 >"))
    print(val1 - val2)
    tryAgain()
  
def addition():
    val1 = int(input("Enter value 1 >"))
    val2 = int(input("Enter value 2 >"))
    print(val1 + val2)
    tryAgain()

def division():
    val1 = int(input("Enter value 1 >"))
    val2 = int(input("Enter value 2 >"))
    print(val1 / val2)
    tryAgain()

login()
