import mysql.connector as con
db = con.connect(host ="localhost", username ="root",password = "", database = "db_atm")
cursor = db.cursor()
login1 = " "
login2 = " "
others = " "
amount_withdrawn = " "
Trans1 = " "
Trans2 = " "
Trans3 = " "
deposit = " "
user1 = " "
ola = " "
receive = " "
sub = " "
balance = " "
deduct1 = " "
deposit = " "
deposit1 = " "
deposit10 = " "
Keyda = ""
def Register():
    First_name = input("Enter your First_Name: ")
    Last_name = input("Enter your Last name: ")
    Username = Last_name + " " + First_name
    Email = input("Enter your email: ")
    Phone_Number = int(input("Enter your Phone_number: "))
    Pin = input("Enter your Four digit pin: ")
    query = "INSERT INTO user (First_Name, Last_Name, Username,Email, Phone_Number, PIN) VALUES (%s,%s,%s,%s,%s,%s)"
    values = (First_name , Last_name , Username, Email , Phone_Number , Pin)
    cursor.execute(query,values)
    db.commit()
    print("Your Username is " + Username)
    print("Thank You for Registering with us")

def user():
    global user1
    query = "SELECT User_id FROM user WHERE Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    user1 = cursor.fetchone()



def debit():
    query = "Select Transaction_Type from transaction where Username = %s"
    values = (login1)
    cursor.execute(query,values)
    debit = cursor.fetchone()
    print(debit)

def Receiver_id():
    query = "SELECT User_id FROM user WHERE Username = %s and Email = %s"
    values = (Trans1 , Trans2)
    cursor.execute(query,values)
    global receive
    receive = cursor.fetchone()
    print(receive[0])

def db_login():   
    # db = con.connect(host="localhost ", user ="root",password= "", database = "db_atm")
    # cursor = db.cursor()
    query ="SELECT * FROM user where Username = %s and PIN = %s"
    # date = INSERT INTO user ("User_id", "First_Name", "Last_Name","Email", "Phone_Number", "Balance") VALUES (%s,%s,%s,%s)
    values = (login1 , login2)
    cursor.execute(query,values)
    product = cursor.fetchall()
    print(product)
    if len(product) <= 0:
       return  print("No Data Found")
    else:
        menu()   
    
def login():
    global login1
    global login2
    login1 = input("Enter your Username ") 
    login2 = int(input("Enter your Pin "))
    db_login()
    
def menu():    
    print(" 1. Balance \n 2. Deposit \n 3. Withdraw \n 4. Transfer ")
    menu = input("Select an Option ")
    if menu == "1":
        Balance()
    elif menu == "2":
        Deposit()    
    elif menu == "3":
        Withdraw()
    elif menu == "4":    
        Transfer()        
    else:
        print("Invalid Selection")

def Balance():
    db = con.connect(host="localhost ", user ="root",password= "", database = "db_atm")
    cursor = db.cursor()
    query ="SELECT Balance FROM user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    balance = cursor.fetchone()
    print(balance[0])
    # transaction()

def Deposit():
    deposit = int(input("Enter The Amount to want to Deposit: "))
    query = "Select Balance From user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    deposit2 = cursor.fetchone()
    deposit1 = deposit2[0] + deposit
    Deposit_Trans()
    query = "UPDATE user SET Balance = %s  WHERE Username = %s and PIN = %s "
    values = ( deposit1 , login1 , login2)
    cursor.execute(query,values)
    db.commit()
    query = "Select Balance From user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    deposit10 = cursor.fetchone()
    Keyda = deposit10[0]
    print("Your deposition was successful" )

   
def Deposit_Trans():  
    global user1
    global deposit
    global deposit1
    query = "Select Balance From user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    deposit2 = cursor.fetchone()  
    query = "SELECT User_id FROM user WHERE Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    user1 = cursor.fetchone()
    # query = "Select Balance From user where Username = %s and PIN = %s"
    # values = (login1 , login2)
    # cursor.execute(query,values)
    # deposit10 = cursor.fetchone()
    # print(deposit10[0])
    query = "INSERT INTO transaction(User_id, Username,Transaction_Type , Transaction_Performed , Initial_Balance, Final_Balance, Amount, Receivers_id , Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (user1[0], login1 ,"Credit", "Deposit" , deposit1[0] , Keyda  , deposit , receive[0] , "Successful")
    cursor.execute(query,values)
    db.commit()      

def Withdraw():
    print("1. #500 \n 2. #1000 \n 3. #2000 \n 4. #5000 \n 5. #10000 \n 6. #20000 \n 7. Others")
    withdraw = input("Select The Amount You want to Withdraw: ")
    if withdraw == "1":
        global amount_withdrawn
        amount_withdrawn = 500
        withdraw_money()
        print("You have successfully withdrawn #500")
    elif withdraw == "2":
        amount_withdrawn = 1000
        withdraw_money()        
        print("You have successfully withdrawn #1000") 
    elif withdraw == "3":
        amount_withdrawn = 2000
        withdraw_money()        
        print("You have successfully withdrawn #2000")    
    elif withdraw == "4":
        amount_withdrawn = 5000
        withdraw_money()
        print("You have successfully withdrawn #5000") 
    elif withdraw == "5":
        amount_withdrawn = 10000
        withdraw_money()
        print("You have successfully withdrawn #10000") 
    elif withdraw == "6":
        amount_withdrawn = 20000
        withdraw_money()        
        print("You have successfully withdrawn #20000") 
    elif withdraw == "7":
        Others()  
    else:
        print("invalid option")     
                                  
def withdraw_money():
    query = "Select Balance from user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    result = cursor.fetchone()
    sql()
    sub = result[0] - amount_withdrawn
    query = "UPDATE user SET Balance = %s  WHERE Username = %s and PIN = %s "
    values =  (sub , login1 , login2) 
    cursor.execute(query,values)
    db.commit()

def sql():
    global user1
    global balance
    query = "Select Balance from user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    result = cursor.fetchone()    
    query = "SELECT User_id FROM user WHERE Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    user1 = cursor.fetchone()
    query = "INSERT INTO transaction(User_id, Username,Transaction_Type , Transaction_Performed , Initial_Balance, Final_Balance, Amount, Receivers_id , Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (user1[0], login1 ,"Debit", "Withdrawal" , result[0] , sub , amount_withdrawn , receive[0],"Successful")
    cursor.execute(query,values)
    db.commit() 
  
def Transfer():
    global Trans1
    global Trans2
    global Trans3
    Trans1 = input("Please Type the Username Of The Person You Want to Transfer to: ")
    Trans2 = input("Please Type the Email of The Person You want to Transfer to: ")
    Trans3 = int(input("Please Enter The Amount you Transfer: "))
    transfer_check()
    transfer_deduction()

def transfer_deduction():
    query = "Select Balance from user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    deduct = cursor.fetchone()
    deduct1 = deduct[0] - Trans3
    Transfer_table()
    print("Your Transfer was Successful")
    query = "UPDATE user SET Balance = %s  WHERE Username = %s and PIN = %s "
    values = (deduct1 , login1 , login2)
    cursor.execute(query,values)
    db.commit()
    

def transfer_check():
    query = "Select Balance from user where Username = %s and Email = %s"
    values = (Trans1 , Trans2)
    cursor.execute(query, values)
    transfer = cursor.fetchone()
    trans12 = transfer[0] + Trans3
    query = "UPDATE user SET Balance = %s  WHERE Username = %s and Email = %s "
    values = ( trans12 , Trans1 , Trans2)
    cursor.execute(query,values)
    db.commit()

def Transfer_table():
    global Trans3
    global deduct1
    global user1
    global balance
    global receive
    query = "SELECT User_id FROM user WHERE Username = %s and Email = %s"
    values = (Trans1 , Trans2)
    cursor.execute(query,values)
    receive = cursor.fetchone()
    query ="SELECT Balance FROM user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    balance = cursor.fetchone()
    query = "SELECT User_id FROM user WHERE Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    user1 = cursor.fetchone()
    query = "INSERT INTO transaction(User_id, Username,Transaction_Type , Transaction_Performed , Initial_Balance, Final_Balance, Amount, Receivers_id , Status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (user1[0], login1 ,"Debit", "Transfer" , balance[0] , deduct1 , Trans3 , receive[0] , "Successful")
    cursor.execute(query,values)
    db.commit() 

def Others():
    global others
    others = int(input("enter amount :"))
    query = "Select Balance from user where Username = %s and PIN = %s"
    values = (login1 , login2)
    cursor.execute(query,values)
    result = cursor.fetchone()
    sub = result[0] - others
    print(result[0])
    print(sub)
    query = "UPDATE user SET Balance = %s  WHERE Username = %s and PIN = %s  "
    values =  (sub , login1 , login2) 
    cursor.execute(query,values)
    db.commit()
    print("You have successfully withdrawn #" + others)

def home():
    print("WELCOME TO YAHOO BANK \n 1. Register \n 2. Login")
    in1 = input("Select an Option ")
    if in1 == "1":
        Register() 
    elif in1 == "2":
        login()
    else:
        print("Invalid Option") 

home()




  


