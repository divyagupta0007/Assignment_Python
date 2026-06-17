while(True):

    studentName = input(str("Enter your Name: "))
    maths = int(input("Marks Scored in Maths: "))
    english = int(input("Marks Scored in English: "))
    chemistry = int(input("Marks Scored in Chemistry: "))
    biology = int(input("Marks Scored in Biology: "))
    physics = int(input("Marks Scored in Physics: "))
    

    if (maths > 100 and english > 100 and chemistry > 100 and biology > 100 and physics > 100):
        print("\n MARKS CANNOT BE MORE THAN 100 \n")

    elif (maths < 100 and english < 100 and chemistry < 100 and biology < 100 and physics < 100):
        break

# Total marks
totalMarks = (maths + english + chemistry + biology + physics) 
print(f"Total Marks: {totalMarks}/500")

# Percnetage
percentage = (totalMarks/500)*100
print(f"Percentage: {percentage:.2f}")

# Grade
if percentage > 90:
    print("A Grade")

elif percentage > 70:
    print("B Grade")

elif percentage > 50:
    print("C Grade")

elif percentage > 30:
    print("D Grade")


# Pass/Fail Status

if percentage > 30:
    print("PASSED")

else:
    print("FAILED")