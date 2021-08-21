import string

inputstr=input('Enter the string: ')
s=set(inputstr)
for i in s:
    x = inputstr.count(i)
    print(i, end=': ')
    print(str(x))