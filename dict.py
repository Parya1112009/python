price = {"mango": 24,"apple": 25,"banana": 20}
product = input("enter the product you want to buy : ")
if product in price:
    print (f"the price of {product} is {price[product]}")
else:
    print("this product is not available today SORRY!!!")  
pricee = {"mango": 24,"apple": 125,"banana": 20,"grapes": 90}      
print("**************after for loop the list is**********************")
high_price = 0
costly_fruit = " "
for k,v in pricee.items():
    print(k,v)
    if v > high_price:
        high_price = v
        costly_fruit = k
print(f"costly fruit is {costly_fruit} with highest price {high_price}")    
price.update(pricee)
print (price)
#for k in price.keys():
#for k in price:
 #   print (k)    
#for v in price.values():
 #   print (v)



