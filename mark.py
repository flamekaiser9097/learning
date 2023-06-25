
def calculatingpercentageTotal():
   return 1
def inputofmarks():
   subjectName=input("enter the name of subject")
   marks=int(input("please enter the subject marks"))
   subject["name"]=subjectName
   subject["marks"]=marks
   subjects.append(subject)
   totalmarks=totalmarks+marks
   subjectFlag=input("do you have any other subject data y/n")


def takestudentInput():
    student={}
    studentName=input("enter student name")
    student["name"]= studentName
    subjectFlag="y"
    subject={}
    subjects={}
    while(flag=="y"):
      takestudentInput()
    calculatingpercentageTotal()
##intilizing variable
students=[]
flag="y"
while(flag=="y"):
    takestudentInput()