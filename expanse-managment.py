def authentication(userName, password): #created a function and passed two arguments

    valid_username = "Sanjay"
    valid_password = "Sanjay"

#Build a condition to check validation

    if userName == valid_username and password == valid_password: 
        print("Authentication successful!")
        return True
    else:
        print("Authentication failed. Invalid username or password. Please entet the correct ")
        return False
    
#taking input from the user
user = input("Enter your username: ") 
pwd = input("Enter your password: ")

def createFile():
    file = open ("expanse.txt", "x")
    data = "name","department","Salary""date","category","description","amount"
    file.write(data)
def listing():
    date = input("please enter date of expanse: ")
    category = input("please enter the category of expanse: ")
    description = input("Please enter the description for the expanse: ")
    amount =input("please enter the amount of expanse: ")
    data = "date of expanse: " + date + "\n"+"category of expanse: " + category +  "\n"+"Description of expanse: " + description + "\n"+ "amount of expanse: " + amount 
    return data

def file(data):
    file = open("expanse.txt", "a")
    data = "\n" + data
    file.write(data)
    
def readFile():
    file = open("expanse.txt", "r")
    data = file.read()
    print(data)

authentication(user, pwd)
readFile()
data = listing()
file(data)