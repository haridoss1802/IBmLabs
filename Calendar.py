#                                                           LCM
'''def lcm(x,y):
    greater=x if x>y else y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter the number1"))
num2=int(input("Enter number2"))
print("The lcm(num1,num2))'''
#                                                          CALENDAR
'''import calendar
month=int(input("Enter month"))
year=int(input("Enter year"))
print(calendar.month(year,month))
print(calendar.calendar(year))'''
#                                                        FACTORIAL
'''n=int(input("Enter number"))
factorial=1
if n<0:
    print("Enter positive integers")
elif n==0:
    print(factorial)
else:
    for i in range(1,n+1):
        factorial =factorial *i
    print(factorial)'''
'''a=1+2+3\
    4+5+6
    print(a)'''
"""if True:
    print("true")"""
#                                               MULTIPLE VARIABLE DECLARATION
'''num1,num3,string1=10,30.0,"sting"
print(type(num1))
#print(c)
print(num3)
print(string1)'''
#                                               LIST, TUPLE
'''a=[1,2,"string"]
t=(1,2,"string")
print(a[0])
print(a[0:3])
print(t[0:2])
set1=(1,1,2,2,2,3,3)
print(set1)
'''
#                                                        STRINGS
b="hello hari"
print(b[0:5])
#                                                      COVERSION
# implicit conversion is done by the computer
# explicit is done by the users
'''a,b=3,2
print(int(a/b),a,b)
print('value of a is {} and b is {}'.format(a,b))
print('value of a is {a1} and b is {b1}',a1=10,b1=20)
list=[1,2,3]
set=(1,2,3,4,5)
tuple1=tuple(list)
print(tuple1)
print(eval(2+3))
print(int(2+3))'''
#                                                         import
# from file_name import class_name:
'''import calendar
calendar.path'''
'''print(2**3) #power function
# is, is not,in,not in
a='hari'
b='doss'
print('h' in b)'''
#               https://www.programiz.com/
dec=int(input(""))
print(bin(dec))