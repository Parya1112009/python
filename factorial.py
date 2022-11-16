from turtle import numinput
def facto( n ):
#    assert n<0 and int(n) != n , "cant calculate the factorial of this number"
    if (n == 1):
        return 1
    elif (n>1):
        return n * facto(n-1)
num = input("enter the number")
factorial = facto(int(num))
print (f"the factorial of {num} is {factorial}!!!")
