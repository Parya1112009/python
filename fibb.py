def facto( n ):
    if (n < 1):
        return 1
    elif (n>=1):
        return (facto(n-1)+facto(n-2))
num = input("enter the number")
for i in range(int(num)):
    print (facto(i))
