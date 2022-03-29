students = []
student = {
	"id" : None,
	"name" : None,
	"DoB" : None
}


def ListStudent():
	numStudent = input("How many student in your class: ")
	return

def StudentInfo():
	studentList= []
	for i in range (numStudent):
		print ("student no "+ " ", i+1)
		id = input ("id:")
		name = input ("name")
		DoB = input ("Date of birth: ")

		student = {
			"id" : id ,
			"name" : name,
			"DoB" : birthday
		}
		students.append(student)
	


def numberOfCourse():
	return (input("Enter the number of course:"))

def courseInfo():
	courseList =[]
	id_course = input ("please enter the id of course:")
	name_course = input ("enter name of course:")
	course = {
		"id_course" : courseId,
		"name_course" : courseName
	}
	courseList.append(course)

def findStudent():
       
        for i in range(0, len(sv.students)):
            if sv.students[i]['id'] == id:
                
                return [i, sv.students[i]]
        return False

def markcourse(course, students):
	if student == 0:
		print ("no student learn this course")
	else: 
		for i in range (len(students)):
			student = sv.findStudent(sv,id)
			mark = input ()

def ShowListcourse():
	print ("list course we have:")
	for i in range (0, len(courseList)):
		print ("[",courseList[i]['id_course'],"]", "[",courseList[i]['name_course'],"]")

def ShowListStudent():
	print ("list student in this class:")
	for i in range (0, len(students)):
		print ("[",students[i]['id'],"]", "[",students[i]['name'],"]")

ListStudent()
StudentInfo()

numberOfCourse()
courseInfo()

markcourse()
ShowListcourse()
ShowListStudent()