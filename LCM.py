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
#                                                           HCF
def compute_hcf(x,y):
    if x>y: smaller=x
    else:   smaller=y
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    return hcf
x=int(input("Enter the number"))
y=int(input("Enter another number"))
print(compute_hcf(x,y))