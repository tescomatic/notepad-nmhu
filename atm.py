# elif(in4 == 2):   
#     print('Welcome To First Bank' '\n 1. Enter Pin? \n 2. Cancel')
#     in1 = int(input("Select Your Option "))
#     if(in1 == 1):
#         for inf in General_list:
#             in2 = input('Enter Your Pin ')
#             if inf == Register :
#                 print("""
#     1. BALANCE
#     2. WITHDRAW
#     3. DEPOSIT
#     4. TRANSFER
#     5. EXIT
#                  """)
#                 option = int(input('Select Your Option '))
#                  if(option == 1):
#                      print("Your Balance is: ",default_bank_balance)
#                  elif(option == 2):
#                      print("""
#      500      10000
#      1000     20000
#      5000     50000         
#                      """)
#                       print("""
#       1. 500      4. 10000
#       2. 1000     5. 20000
#       3. 5000     6. 50000 
#           7. OTHERS         
#                      """)
#                     withdraw = int(input("Select Your Option: "))
#                     if(withdraw == 1):
#                          new_balance = ba
#                          print('Sucesss')
#                          print('Your New Balance is: ',)    
#                     withdraw = int(input("Enter Amount you want to withdraw "))
#                     if(default_bank_balance > withdraw):
#                         new_balance = default_bank_balance - withdraw
#                         print('Success')
#                         print('Your New Balance is: ',new_balance) 
#                     else:
#                         print("Theif,Go work Joor")      
#                 elif(option == 3):
#                     pick = int(input("Enter Amount you want deposit "))
#                     new_balance = default_bank_balance  + pick
#                     print("Success")  
#                     print("Your New Balance is: ",new_balance) 
#                 # elif(option == 4):

#             elif len(in2) > 4:
#                 print("Pin greater than four digits")
#             else:
#                 print("Pin lesser than four digits")
#     else:
#         print('Thank You For Using First Bank')   

General_list = []
Register = {}
in1=''
default_bank_balance = 30000
def regi():
    print('Please Enter Your FullName,Account Number,Pin')
    Full_name = input('Enter your Full_name: ')
    Pin = input('Enter your four digits Pin: ')
    Email = input('Enter your email: ')
    Register['Full_name'] = Full_name
    Register['Pin'] = Pin
    Register['Email'] = Email
    General_list.append(Register)
    print(Register)
    print(General_list)


def menu():
        print("""
1. BALANCE
2. WITHDRAW
3. DEPOSIT
4. TRANSFER
5. EXIT
                """)
def balance():
    if(option == 1):
        print("Your Balance is: ",default_bank_balance)

def withdraw():
    if option == 2:
        print("""
500      10000
1000     20000
5000     50000         
""")  
        withdraw = int(input("Enter Amount you want to withdraw "))
        if(default_bank_balance > withdraw):
            new_balance = default_bank_balance - withdraw
            print('Success')
            print('Your New Balance is: ',new_balance) 
        else:
            print("Theif,Go work Joor")


def deposit():
    if(option == 3):
        pick = int(input("Enter Amount you want deposit "))
        new_balance = default_bank_balance  + pick
        print("Success")  
        print("Your New Balance is: ",new_balance)
    else:
        print("Try Again Later") 


# def Transfer():









print("""WELCOME TO FIRST BANK
1. Register an Account""")
in4 = input("Select Your Option ")
if in4 == "1":
    regi()
    print("1. Please Log In")
    in1 = input('Enter Your Full_name')
    if in1 == :
        print('Welcome To First Bank' '\n 1. Enter Pin? \n 2. Cancel')
        in1 = input('Select Your Option')
        in2 = input('Enter Your Pin ')
        for i in Register:
            if Register["Pin"] == in2:                
                menu()
                option = int(input('Select Your Option '))
                balance()
                withdraw()
                deposit()
                print(default_bank_balance)
                break
    #             elif(option == 2):
    #                 print("""
    #  500      10000
    #  1000     20000
    #  5000     50000         
    #                  """)
            else:
                print("Try Again Later")
                break
    else:
        print("Try Again Later")             
else:
    print("Try Again Later")         
# import mysql.connector as con
# db = con.connect(host ="localhost", username ="root",password = "", database = "db_atm")
# cursor = db.cursor()

# def login():
#     in4 = input("Enter your First_Name") 
#     in5 = int(input("Enter your Pin"))
#     db_login()
    
# def Register():
#     First_name = input("Enter your First_Name: ")
#     Last_name = input("Enter your Last name: ")
#     Email = input("Enter your email: ")
#     Phone_Number = input("Enter your Phone_number: ")
#     Pin = int(input("Enter your Four digit pin"))
#     query = "INSERT INTO user (First_Name, Last_Name,Email, Phone_Number, PIN) VALUES (%s,%s,%s,%s,%s)"
#     values = (First_name , Last_name , Email , Phone_Number , Pin)
#     cursor.execute(query,values)
#     db.commit()

    
# def db_login():   
#     db = con.connect(host="localhost ", user ="root",password= "", database = "db_atm")
#     cursor = db.cursor()
#     query ="SELECT * FROM user where First_Name = %s and PIN = %s"
#     # date = INSERT INTO user ("User_id", "First_Name", "Last_Name","Email", "Phone_Number", "Balance") VALUES (%s,%s,%s,%s)
#     values = (in4 , in5)
#     cursor.execute(query,values)
#     cursor.fetchall()


# def home():
#     print("WELCOME TO YAHOO BANK \n 1. Register \n 2. Login")
#     in1 = input("Select an Option ")
#     if in1 == "1":
#         Register() 
#         print("Thank You for Registering with us")
#     elif in1 == "2":
#         login()
#     else:
#         print("Invalid Option") 




# home()   