import math
def sqrt():
    n=int(input("Enter a number\n"))
    s=math.sqrt(n)
    print("Square root of ",n," is ",s)
    return
def division():
    a=int(input("Enter 1st number"))
    b=int(input("Enter 2nd number"))
    s=a/b
    print(s)
    return
print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division\n5.Square-Root\n6.Power\n7.exit\n")
op=0
while op<7:
    op=int(input("Enter Your Option!\n"))
    match op:
        case 1:
            print("Work In Progress")
        case 2:
            print("Work In Progress")
        case 3:
            print("Work In Progress")
        case 4:
            division()
        case 5:
            sqrt()
        case 6:
            print("Work In Progress")
        case default:
            print("Thank You")


