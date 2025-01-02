from task1 import *

menu = """

Press 1 for Reverse Number 
Press 2 for Pattern
Press 3 for Addtion 
Press 4 for Factorial 
Press 5 to Exit

"""

while True:
    print(menu)

    choice = int(input("Enter a Choice : "))

    if choice == 1:

        n = int(input("Enter Number : "))
        fun1(n)

    elif choice == 2:

        fun2()

    elif choice == 3:

        fun3()

    elif choice == 4:
        n = int(input("Enter A Number : "))
        print("The Facotrial is : ", fun4(n))
        

    elif choice == 5: 
        print("Thank You !!")
        break


    else: 
        print("Invalid Input !!!")
        break