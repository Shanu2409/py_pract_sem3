# append a text and display the file

file = open("some.txt", "a")
txt = input("Enter a text to append in some.txt : ")
file.write('\n' + txt)
file.close()
file = open("some.txt", "r")
print("After adding our text")
print(file.read())
file.close()
