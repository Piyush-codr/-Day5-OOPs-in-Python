class Student:
    def __init(self):
        self.__sid = None
        self.__age = None
        self.__mark = None
    def validate_marks(self):
        if self.__mark<=100 and self.__mark>=0:
            return True
        else:
            return False
    def validate_age(self):
        if self.__age>20:
            return True
        else:
            return False
    def check_qualifications(self):
        if self.validate_age() and self.validate_marks() and self.__mark>=65:
            return True
        else:
            return False
    def discount_applicable(self):
        if self.check_qualifications() and self.__mark>85:
            print("25% Discount Applicable")
        else:
            print("No discount applicable")
    def get_sid(self):
        return self.__sid
    def get_age(self):
        return self.__age
    def get_mark(self):
        return self.__mark
    def set_sid(self,sid):
        self.__sid=sid
    def set_age(self,age):
        self.__age=age
    def set_mark(self,mark):
        self.__mark=mark
s1 = Student()
s1.set_sid(186)
s1.set_age(22)
s1.set_mark(89)
s1.check_qualifications()
s1.discount_applicable()
s1.set_mark(50) 
print(s1.check_qualifications())
s1.discount_applicable()
