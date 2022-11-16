dict1 = {"name":"priya","sname":"arya","kids":["yuvan","eva"],"husband":"ravi"}
dict2 = {"mom":"santosh","dad":"rajendra","bro":{"bro1":"chotu","bro2":"guddu"},"sis":1}
dict3 = {**dict1,**dict2}
list = [{"friend":"palak","bff":"neha"},{"office":"cisco","location":"fremont"}]
print("my friend is")
print(list[1]["office"])
print (dict3)
print("my brother2 is")
print (dict2["bro"]["bro2"])
print("my brother1 is")
print (dict2["bro"]["bro1"])