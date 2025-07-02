standard_list = []      #defining the list
#list can contain multiple types of data
standard_list = [1,2,'mehul', True, 4.0]  
print(f"The list is {standard_list}")  
print(type(standard_list))      #class of list is always = list (irrespective of data entered inside)

print(standard_list[0])         #accessing the first element of the list

print(standard_list[0:5])       #format is (start : end : step)
print(standard_list[:5])        #by default starts from first element
print(standard_list[0:])        #by default ends at last element
print(standard_list[0:5:2])

print(standard_list[::-1])      #printing in reverse order
print(standard_list.reverse())  #same function

#loop through standard_list data to get each line
for x in standard_list:
    print(f'data value from list is {x}')

stand_list = [100,['mehul',200,'gurugram'],['manan','gurgaon']]       #defining list in list
print(stand_list)
print(stand_list[1])        #to get info about mehul
print(stand_list[1][2])     #to get specific info about mehul

stand_list.append(500)      #to add value to a list at the end. Append can add only one type of data
print(stand_list)

#stand_list.extend(100,'mukul')         this will give an error as extend function only takes one argument
stand_list.extend([100,'mukul'])        #the statemnt can be written as a single list
print(stand_list)

#the same program can be written as
list_extend = [300,'mgupta']
stand_list.extend(list_extend)
print(stand_list)

stand_list.insert(2,5000)               #to insert a value in a list at a specific position (position, value)
print(stand_list)

print(stand_list.index(5000))           #to find position of a value

stand_list.pop(2)                       #to remove value from list using the position
#stand_list.pop() to remove the end value of a list
print(stand_list)

stand_list.remove(100)                  #to remove value from list using the value
print(stand_list)

print(stand_list.clear())               #to clear values from the list