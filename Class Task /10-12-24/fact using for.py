n = int(input("Enter a Number : "))

fac = 1

for i in range(1,n+1,1):
    fac*=i

print(fac)


for i in range(1,n+1,1):
    if n%i==0:
        c+=1

if(n==2):
    print("Number is Not Prime!!!")

elif(c==2):
    print("Number is Prime !!")

else:
    print("The Number is Not Prime !!")
