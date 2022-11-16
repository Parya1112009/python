import pdb;
def great(num,num2):
    assert int(num)==num and int(num2)==num2, "enter the integer numbers"
    if num<0:
       num = num * -1
    if num2==0:
        num2 = num2 * -1   
    if num2==0:
       return num

    else:
        return (great(num2,num%num2))
print(great(48,0))
        