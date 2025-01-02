menu = """
Press 1 for Pattern 
Press 2 for String
Press 3 for Palindrome
Press 4 to Exit  
"""
def pattern():
    n = input("Enter Number Of Rows : ")



def string():
    print("Enter Odd String")
    n = input("Enter String : ")

    mid = (len(n))/2
    print(n[mid-1], n[mid] , n[mid+1])


def palindrome():
    n = input("Enter a String : ")
    
    if n[::-1] == n:
        print("The String is Palindrome !!!")

    else:
        print("The String is Not Palindrome !!!")
