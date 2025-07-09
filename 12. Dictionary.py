data_dict= {}                           #defing the dictionary
print(type(data_dict))
data_dict = {
    101 : ['mehul','ggn',10000],        #keys : values
    102 : {True, False},
    103 : (110,'date')
}

for i in data_dict.keys():
    print(data_dict.keys())
    print(data_dict.values())

print(data_dict[101])           #accessing values of a key
print(data_dict[101][0])        #accessing specific value of a key

print(data_dict.items())        #value of each key printed together
for x,y in data_dict.items():
    print(f'key of dictionary is {x} and value is {y}')

for x in enumerate(data_dict.keys()):               #gives the serial order along with the value
    print(x)

for i in data_dict.keys():                          #does not print the keys in serial order
    print(i)

print(data_dict.get(110,'No value present'))        #(to get the values in keys, default value) it is used to continue the program and not give an error


data_dict.update({101:'hotstar'})                   #clears the existing values in a key and new value is updated, if key does not exist then it creates a new key

data_dict.pop(102)                           #pop will return the values
print(data_dict)

print(data_dict.popitem())                          #return values and keys

data_dict.clear()                                   #clears out content of the dictionary