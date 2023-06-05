king=input('enter a string:')


def palindrome(king):
    if king[::-1]==king[:]:
        return 1
    else:
        return 0

j=palindrome(king)
print(j)
