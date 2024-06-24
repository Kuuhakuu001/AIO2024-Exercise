class Person:
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob
    
    def describe(self):
        raise NotImplementedError("Subclasses should implement this!")

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade
    
    def describe(self):
        print(f"Student - Name: {self.name} - YoB: {self.yob} - Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject
    
    def describe(self):
        print(f"Teacher - Name: {self.name} - YoB: {self.yob} - Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    
    def describe(self):
        print(f"Doctor - Name: {self.name} - YoB: {self.yob} - Specialist: {self.specialist}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

    def add_person(self, person):
        self.people.append(person)

    def count_doctor(self):
        return sum(isinstance(person, Doctor) for person in self.people)

    def sort_age(self):
        self.people.sort(key=lambda person: person.yob, reverse=True)

    def compute_average(self):
        teachers = [person for person in self.people if isinstance(person, Teacher)]
        if not teachers:
            return 0
        total_years = sum(teacher.yob for teacher in teachers)
        return total_years / len(teachers)

    def describe(self):
        print(f"Ward Name: {self.name}")
        for person in self.people:
            person.describe()

# Examples 1
student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
# Output: Student - Name: studentA - YoB: 2010 - Grade: 7

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
# Output: Teacher - Name: teacherA - YoB: 1969 - Subject: Math

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
# Output: Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists

# Examples 2(b)
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")

ward1 = Ward(name="Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)

ward1.describe()
# Output:
# Ward Name: Ward1
# Student - Name: studentA - YoB: 2010 - Grade: 7
# Teacher - Name: teacherA - YoB: 1969 - Subject: Math
# Teacher - Name: teacherB - YoB: 1995 - Subject: History
# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists
# Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists

# Examples 2(c)
print(f"Number of doctors: {ward1.count_doctor()}")
# Output: Number of doctors: 2

# Examples 2(d)
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()
# Output:
# Ward Name: Ward1
# Student - Name: studentA - YoB: 2010 - Grade: 7
# Teacher - Name: teacherB - YoB: 1995 - Subject: History
# Doctor - Name: doctorB - YoB: 1975 - Specialist: Cardiologists
# Teacher - Name: teacherA - YoB: 1969 - Subject: Math
# Doctor - Name: doctorA - YoB: 1945 - Specialist: Endocrinologists

# Examples 2(e)
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
# Output: Average year of birth (teachers): 1982.0
