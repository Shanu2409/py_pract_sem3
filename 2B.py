# create function to return the len of string or list

def length(x):
    cnt = 0
    for i in x:
        cnt += 1
    return cnt


str = input("Enter a string : ")
lis = [1, 2, 3, 4, 5]

print(length(str))
