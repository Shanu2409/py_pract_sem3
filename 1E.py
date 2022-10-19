# check for armstrong number and palindrome number
def armstrong(n):
    temp = n
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit ** 3
        temp = temp // 10

    if n == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")


def palindrome(n):
    temp = n
    rev = 0
    while temp > 0:
        dig = temp % 10
        rev = (rev * 10) + dig
        temp = temp // 10

    if n == rev:
        print(str(n) + " is palindrome number")
    else:
        print(str(n) + " is not palindrome number")


num = int(input("Enter a number for armstrong : "))
armstrong(num)


num = int(input("Enter a number for palindrome : "))
palindrome(num)
