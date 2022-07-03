#Question 6
#Student Data

def student_data(student_id,**kwargs):
    print("Student ID=",student_id)
    if "student_name" in kwargs:
        print("Student Name=",kwargs["student_name"])
    if "student_class" in kwargs:
        print("Student Class=",kwargs["student_class"])

student_data(student_id="19102034")
student_data(student_id="19102034",student_name="Moman Sethi")
student_data(student_id="19102034",student_name="Moman Sethi",student_class="1st Year")
print()
