a=int(input("enter the first number : "))
b=int(input("enetr the second number : "))
print("calculator")
print("+ -> Addition")
print("- -> Subtraction")
print("* -> Multiplication")
print("/ -> Division")
c=input("enter your choice")
if c=="+":
    print("the addition of two number is : ",a+b)
elif c=="-":
    print("the Subtraction of two number is : ",a-b)
elif c=="*":
    print("the product of two number is : ",a*b)
elif c=="/":
    if b==0:
        print("Enter a valid number")
    else:
        print("the division of two number is : ",a//b)