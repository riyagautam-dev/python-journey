student={}
for i in range(0,4):
 name=input("Enter student name: ")
 marks=list(map(int,input("enter marks:").split(",")))
 student[name]=marks
print(student)
