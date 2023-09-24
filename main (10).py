class student :

def __init__(self,name,roll_number,cgpa)
   self.name= name 
    self. roll_number = roll_number 
   self. cgpa =cgpa 


def sort_student(student_list): 
   #sort the list of student in descending order of CGPA 
    sorted_student = sorted(student_list) 
          key= lamba student:student.cgpa 
        reverse = True 
    return sorted_students 


#Example usage: 
  students = [ 
      student("Hari","A123",7.8), 
      student("Srikanth","A124",8.9), 
      student("saumya","A125",9.1), 
      student("mahidhar","A126",9.9), 
]