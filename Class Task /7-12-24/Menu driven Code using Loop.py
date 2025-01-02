menu = """
    Press 1 for Addition
    Press 2 for Prime
    Press 3 for Factorial 
    Press 4 for Exit
"""

while True:
    print(menu)

    choice = int(input("Enter Choice : "))

    if choice==1:
        n1 = int(input("Enter a Number  : "))
        n2 = int(input("Enter A Number : "))

        print("addition : ",n1+n2)

    elif choice==2:
        n = int(input("Enter A Number : "))

        if(n%2==0):
            print("Number is Even")

        else:
            print("Number is Odd")

    elif choice==3:
        n = int(input("Enter a number : "))
        i = 1
        fac = 1

        while(i<=n):
            fac*=i
            i+=1

        print("Factorial : ",fac)

    elif choice==4:
        print('Thank You !!')
        break

    
