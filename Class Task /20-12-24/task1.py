def fun1(n):

    remainder = 0
    reverse = 0

    while(n!=0):

        remainder = n%10
        
        reverse = reverse*10+remainder

        n =n//10

    print("The reverse number is : ", reverse)


def fun2():

    n = int(input("Enter a number : "))

    for i in range(1,n+1):
        print(f"{i}"*i)


def fun3():

    n = int(input("Enter a number : "))
    n1 = int(input("Enter a number : "))


    print("Addition of 2 Input : ", n+n1)

