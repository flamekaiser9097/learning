def add(a,b):
   return a+b
def subtract(a,b):
   return a-b
def multiply(a,b):
   return a*b
def divide(a,b):
   return a/b
def modulo(a,b):
   return a%b
operator=input("please input the operator: ")
num1=int(input("please enter number 1: "))
num2=int(input("please enter number 2: "))
if operator == '+':    
   print (num1, " + ", num2, " = ", add(num1, num2))       
elif operator == '-':    
   print (num1, " - ", num2, " = ", subtract(num1, num2))       
elif operator == '*':    
   print (num1, " * ", num2, " = ", multiply(num1, num2))    
elif operator == '/':    
   print (num1, " / ", num2, " = ", divide(num1, num2))
elif operator=="%" :   
   print (num1, " % ", num2, " = ", modulo(num1, num2))
else:    
   print ("This is an invalid input")    
