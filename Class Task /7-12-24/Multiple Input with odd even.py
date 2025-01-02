i = 1
ev = 0
od = 0
evsum = 0
odsum = 0 

while(i<=5):
    n = int(input("Enter a Number"))

    if n%2==0:
        print(n, "Number is Even")
        ev+=1
        evsum+=n

    else:
        print(n,"Number is Odd")
        od+=1
        odsum+=n
        

    i+=1


print("Total Even Numbers : ", ev)
print("Total Odd Numbers : ",od)
print("Sum of Even Numbers : ",evsum)
print("Sum of Odd Numbers : ",odsum)