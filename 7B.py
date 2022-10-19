class Num1:
    def sayHello(self, name):
        print("Hello ", name)


class Num2(Num1):
    def hello(self):
        self.sayHello(__name__)

    def sayBye(self, name):
        print("Bye ", name)


n1 = Num2()
n1.sayHello('shan')
