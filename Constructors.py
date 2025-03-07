class Person:
    def __init__(self):
        self.full_name = "Rahul"  

    def show_name(self):
        print(self.full_name)

person1 = Person()
person1.show_name()


class Student(Person):
    def __init__(self):
        self.full_name = "Aryan"

    def show_student_name(self):
        print(self.full_name)

student1 = Student()
student1.show_student_name()


class Details:
    name = None  
    _id = None  
    __course = None  

    def __init__(self, name, student_id, course):
        self.name = name  
        self._id = student_id  
        self.__course = course  

    def show_details(self):
        print("Name:", self.name)

    def _show_id(self):
        print("ID:", self._id)

    def __show_course(self):
        print("Course:", self.__course)

    def access_course(self):
        self.__show_course()


class ExtraDetails(Details):
    def __init__(self, name, student_id, course):
        super().__init__(name, student_id, course)

    def access_id(self):
        self._show_id()


student2 = ExtraDetails("Rahul", 101, "Computer Science")
student2.show_details()
student2.access_id()
student2.access_course()
