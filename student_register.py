#list maker function to create the list
def list_maker(amount_students):
    student_id=[]
    for i in range(amount_students):
        student_id.append(input("please add the student IDs"))
    return student_id
#program starts here by asking how many student are going to be there
amount_students=int(input("Please add how many students are going to register?"))
#calling the list maker function
student_id=list_maker(amount_students)
#This code creates and writes the text file.
with open('reg_form.txt','w+') as f:
    for item in range(amount_students):
        f.write(student_id[item]+"............"+"\n")
