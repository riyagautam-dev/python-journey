print("Welcome to Student Marks Analyzer")
marks_entered = False
while True:

    print("\n1. Enter Student Marks")
    print("2. View Result")
    print("3. View Failed Subjects")
    print("4. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        print("You have chosen option 1")
        print("Enter the marks of student in subjects")

        english = int(input("Enter marks in English: "))
        while english < 0 or english > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            english = int(input("Enter marks in English: "))

        maths = int(input("Enter marks in Maths: "))
        while maths < 0 or maths > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            maths = int(input("Enter marks in Maths: "))

        science = int(input("Enter marks in Science: "))
        while science < 0 or science > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            science = int(input("Enter marks in Science: "))

        computer = int(input("Enter marks in Computer: "))
        while computer < 0 or computer > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            computer = int(input("Enter marks in Computer: "))

        commerce = int(input("Enter marks in Commerce: "))
        while commerce < 0 or commerce > 100:
            print("Invalid marks. Please enter marks between 0 and 100.")
            commerce = int(input("Enter marks in Commerce: "))
        marks_entered = True
    elif choice==2:
        if not marks_entered:
            print("Please enter student marks first (Option 1).")
            continue
        print("You have chosen option 2")
        print("View Results")

        total_marks=english+maths+science+computer+commerce
        print("Total marks:", total_marks)
        percentage=total_marks/5
        print("Percentage:", percentage, "%" )
        if percentage >= 90:
          print("Grade: A+")
        elif percentage >= 80:
          print("Grade: A")
        elif percentage >= 70:
          print("Grade: B")
        elif percentage >= 60:
          print("Grade: C")
        elif percentage >= 33:
           print("Grade: D")
        else:
            print("Grade: F")


        highest_marks=max(english,maths,science,computer,commerce)
        print("Highest marks:", highest_marks)
        lowest_marks=min(english,maths,science,computer,commerce)
        print("Lowest marks:", lowest_marks)


    elif choice==3:
        if not marks_entered:
            print("Please enter student marks first (Option 1).")
            continue
        failed_subjects=[]
        if english < 33:
          failed_subjects.append("English")
        if maths < 33:
          failed_subjects.append("Maths")
        if science < 33:
          failed_subjects.append("Science")
        if computer < 33:
          failed_subjects.append("Computer")
        if commerce < 33:
          failed_subjects.append("Commerce")
        print("Failed subjects:", failed_subjects)
        if not failed_subjects:
         print("Result: Pass")
        else:
          print("Result: Fail")

    elif choice == 4:
        print("Thank you for using Student Marks Analyzer!")
        break

    else:
        print("Invalid choice!")