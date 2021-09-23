# Dictionary and its function

# Dictionary: Dictionary is nothing but the key value pairs
d1={}
print(type(d1))
d2={"Neha": 100, "Dell":101 ,"john":{"id":16, "sal": 67000}}
print(d2["john"])
d2["Tom"]= 105
print(d2)
del d2["Neha"]
print(d2)
print(d2.keys())
print(d2.items())
d3=d2.copy()
print( d3)
d2.update({"Jerry " : 89})
print(d2)
