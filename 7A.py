class Student:
    def setData(self, name, age, cls, rollNo):
        self.name = name
        self.age = age
        self.cls = cls
        self.rollNo = rollNo

    def getData(self):
        print("name = ", self.name)
        print("age = ", self.age)
        print("class = ", self.cls)
        print("Roll number = ", self.rollNo)


s1 = Student()
s1.setData('shanu', 19, 'BSc IT', 22406)
s1.getData()
