
Total_Courses = int(input("Enter the total number of Courses: "))
print(f"Total Number of Courses: {Total_Courses}")


system = {}

for i in range(1, Total_Courses + 1):

    studentList = []
    teacherList = []


    Course = input(str(f"\nEnter the Name of the Course {i}: "))
    
    Total_Students = int(input(f"\nEnter the total number of Students in Course {Course}: "))
    print(f"Total Number of Students: {Total_Students}")

    Total_Teachers = int(input("\nEnter the total number of Teachers: "))
    print(f"Total Number of Teachers: {Total_Teachers}")

    for i in range(1, Total_Students + 1):

        Student = input(str(f"\nEnter the Name of the Student {i}: "))
        studentList.append(Student)
        # print(studentList)
        
    for i in range(1, Total_Teachers + 1):    

        Teacher = input(str(f"\nEnter the Name of the Teacher {i}: "))
        teacherList.append(Teacher)
        # print(teacherList)

    # for i in range(Total_Students + 1, 1):

        # if (Total_Students >)
        
    
    
    system.update({Course:{"students":studentList,"teacher":teacherList}})


    print(f"\nStudents in Course {Course}: ", studentList)
    print(f"Teachers in Course {Course}: ", teacherList)
    

print("\n")

for x, y in system.items():
    print("Course :", x)

    for i in y:
        print(i, ":", y[i])
