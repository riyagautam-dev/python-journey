english=int(input("Enter marks in English: "))
maths=int(input("Enter marks in Maths: "))
science=int(input("Enter marks in Science: "))
computer=int(input("Enter marks in Computer: "))
commerce=int(input("Enter marks in Commerce: "))
computer=int(input("Enter marks in Computer: "))

total_marks=english+maths+science+computer+commerce
print("Total marks:", total_marks)
percentage=total_marks/5
print("Percentage:", percentage, end="%" )
highest_marks=max(english,maths,science,computer,commerce)
print("Highest marks:", highest_marks)
lowest_marks=min(english,maths,science,computer,commerce)
print("Lowest marks:", lowest_marks)
if english >=33 and maths >=33 and science >=33 and computer >=33 and commerce >=33:
    print("Result: Pass")
else:
    print("Result: Fail")