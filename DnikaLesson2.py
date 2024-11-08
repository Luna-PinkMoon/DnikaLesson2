class Student:
  def __int__(self, first_name, last_name, student_id, age, grade):
    #define initialisation - the first one has been done for you
    self.first_name = first_name
    #create an array to store the courses
    self.courses = []
    self.attendance = {}

  #function for course enrolled
  def course_enrollment(self, course):
    self.courses.append(course)

  #function for calculating the total grades. this should return the average grade
  def calculate_average_grade(self):
    total_grades = sum(...)
    return ...

  #function for recording the attendance
  def record_attendance(self, course, attendance):
    self.attendance[course] = ...

class Course:
  def __init__(self, course_name, course_id):
    #define initialisation - the first one has been done for you
    self.course_name = course_name
    ....

  # function to add students
  def add_student(self, student):
    self.students.append(student)
    student.course_enrollment(self)

  #function to add grades
  def assign_grade(sefl, student, grade):
    self.grades[student] = grade
