import pdb
dict1 = {"mom" : {"name":"priyanka","age":"28"},"baby":{"name":"eva","age":"28"},"hubby":"ravi"} 
#dict1 = {"mom" : {"name":"priyanka","age":"28","baby":{"name":"eva","age":"28"}},"hubby":"ravi"} 
def flatten_dict(dict1):
  def expand(key,value): 
    if isinstance(value,dict):
      return [(key + '.' + k,v) for k,v in flatten_dict(value).items()]
    else:
      return [(key,value)]
  #items = [item for k,v in dict1.items() for item in expand(k,v)]
  items = []
  for k,v in dict1.items():
      pdb.set_trace()
      for item in expand (k,v):
          items.append(item)
  print (dict(items)) 
  return (dict(items)) 
print (flatten_dict(dict1)) 

