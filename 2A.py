# return true if vowels

def isVowels(s):
    if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
        return True
    else:
        return False


ch = input("Enter a char : ")

if isVowels(ch.lower()):
    print("It's a Vowels...")
else:
    print("It's not a Vowels")
