    

class Course:
    
    C = ""
    T = ""
    S = []

    def input_C():

        Course.C = (str(input(f"Enter the Name of Course: ")))


    class Teacher:

        def input_T():

            Course.T = str(input(f"Enter the Name of the Teacher for the Course: "))


    class Student(Teacher):

        def input_S():

            Course.S = []
            tol = int(input(f"Enter the Total Number of the Students for the Course: "))      

            for i in range(1, tol + 1):
             
                Course.S.append(str(input(f"Enter the Name of the Student {i} for the Course: ")))       
                print(Course.S)

            print(f"\n\n Course: {Course.C} \n Teacher: {Course.T} \n Students: {Course.S} \n")


# data = int(input("Enter the number of Courses: "))


a = int(input(f"Enter the Total Number Courses: "))       

for i in range(1, a + 1):

    Course.input_C()
    Course.Teacher.input_T()
    Course.Student.input_S()




