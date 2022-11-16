prices = {"mango": 24,"apple": 25,"banana": 20}
product = input("enter the product you want to buy : ")
price = prices.get(product)
if price: 
    print (f"the price of {product} is {price}")
else:
    print("this product is not available today SORRY!!!")    
del prices["apple"]
print (prices)
prices["apple"] = 40
print (prices)
prices.pop("mango")
print(f"pop will remove the value of key mango,the final dictionary is\n {prices}")
prices["mango"] = 49
prices["apple"] = 49
prices.popitem()
print(f"popitem will remove the value of most recent key value pair, the final dictionary is\n {prices}")
prices.clear()
print(f"clear will empty the dictionary , the final dictionary is \n{prices}")
