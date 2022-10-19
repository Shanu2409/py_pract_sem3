# fibonacci numbers

num1 = 0
num2 = 1

for i in range(10):
    print(num1, end=" ")
    num1, num2 = num2, num1 + num2
