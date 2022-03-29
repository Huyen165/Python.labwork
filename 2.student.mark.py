 
studentList= []
courseList = []
class Student:      
    def StudentInfo():
        
        NumberOfStudent = int(input("How many students in this class?"))
        
        for i in range (NumberOfStudent):
                print("student no "+ " ", i+1)
                id = input ("id:")
                name = input ("name:")
                DoB = input ("Date of birth: ")

                student = {
                    "id" : id ,
                    "name" : name,
                    "DoB" : DoB
                }
                studentList.append(student)
    

    def courseInfo():
        numberOfCourse = int(input("Enter the number of course:"))
        for j in range (numberOfCourse):
            print("subject no "+ " ", j)
            id_course = input ("please enter the id of course:")
            name_course = input ("enter name of course:")
            course = {
                "id_course" : id_course,
                "name_course" : name_course
            }
        courseList.append(course)    
        
    def ListStudent():
        for i in studentList:
            print("Student", i)
        

    def ListCourse():
       for j in courseList:
          print("course info: ", j)

    
    StudentInfo()
    ListStudent()
   
    
    courseInfo()
    ListCourse()