# Write a program that takes two lists and returns True if they have at least one
# common member.

def common(a, b):
    for i in b:
        if i in a:
            return (True, i)
    return False


a = [1, 14, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [22, 43, 643, 14]

print(common(a, b))
