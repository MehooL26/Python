#tuple is not mutable so it is used in cases of host name, user admin name etc.

data = ()  #defining a tuple
print(type(data))       #data type is tuple
data = (10)             #data type will be int
print(type(data))
data = (10,)            #now data type will be tuple
print(type(data))
