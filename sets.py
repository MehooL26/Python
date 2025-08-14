data_set = set()            #defining the set
#set removes duplicate data
d1 = {1,3,5,7,9}
d2 = {2,3,6,8,10}
print(type(d1))

d3 = d1.add(12)
#print(d3)   add method does not return the value and we can only add single argument
print(d1)


d4 = d1.difference(d2)
print(d4)

d5 = d1.intersection(d2)
print(d5)

print(d2.issubset(d1))

d6 = d1.issuperset(d2)

print(d1 & d2)      #intersection
print(d1 | d2)      #union
print(d1^d2)        #A union B - A intersection B

d7 = d1.update(d2)      #can add multiple arguments as a single argument
#can also be written as
d7 = d1.update({2,3,6,8,10})

print(d2.pop())         #deletes random values

d8 = d1.discard(3)      #deletes value irrespective of the value present in the set or not
print(d8)

d9 = d1.remove(9)       #deletes value only if it is present in the set
print(d9)