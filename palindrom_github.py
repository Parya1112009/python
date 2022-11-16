
str = input("entr the number") 
k = len(str)/2 -1 
print (k)
count = 0
i=0 
while i<=k:
 if str[i] ==str[-i-1]:
   count = count +1 
 i= i+1
if count>k:
  print ("string is palindrom")
else:
  print ("%s string is not palindrom")
