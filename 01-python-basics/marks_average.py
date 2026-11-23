student={}
for i in range(0,3):
 name=input("Enter student name: ")
 marks=list(map(int,input("enter marks:").split(",")))
 student[name]=marks
for name,marks in student.items():
 total=sum(marks)
 average=total/len(marks)
 print(name)
 print("total:",total)
 print("average:",average)
 if(average>=40):
  print("pass")
 else:
  print("fail")