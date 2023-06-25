def printName(name):
    print(student["name"])
    student["age"]=20
    subject="english"
    return (student["age"]-2)




#executing the function
student={
    "name":"sanjay",
    "age":23,
    "phone":"1234567890"
}
subject="maths"
# printName("sohail", 35, "1234567890") 
print(student["age"],subject)
modifiedAge = printName(student)
# print(modifiedAge)
print(student["age"],subject)