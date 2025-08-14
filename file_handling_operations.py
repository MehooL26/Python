f = open("/Users/mehulgupta/Documents/Python/records.txt",'r')       #opening a file
#file_data = f.read()           reads the document and prints the characters by separating them by \n
#file_data = f.readline()       reads only one line and prints the characters by separating them by \n(the bracket in the syntax contains storage in bytes)
file_data = f.readlines()      #reads all the lines and prints them exactly how the document is written
print(type(file_data))
for x in file_data:
    print(x)
f.close()                      #closes a file'''

'''linux commands in terminal

.. = step back
. = current
/ = directory
pwd = present working directory
ls = list file
ls-lrt = list file in reverse order of time
ls-a = show hidden files    '''


#printing only one column
f = open('/Users/mehulgupta/Documents/Python/records.txt','r')
file_data = f.readlines()
result = []
for x in file_data:
    result.append(x.split(","))
for y in range(len(file_data)):
    print(result[y])
for z in range(len(result)):
    print(result[z][1])
f.close()

#printing 2 columns together
f = open('/Users/mehulgupta/Documents/Python/records.txt','r')
file_data = f.readlines()
result = []
for x in file_data:
    result.append(x.split(","))
for y in range(len(file_data)):
    print(result[y])
for z in range(len(result)):
    print(f'{result[z][1]}      {result[z][3]}')

#checking whether can we write something in read mode
f = open('/Users/mehulgupta/Documents/Python/records.txt','r')
f.write('hello')
f.close()
#output : error

#checking whether can we read something in write mode
f = open('/Users/mehulgupta/Documents/Python/records.txt','w')
file_data = f.readline()
print(file_data)
f.close()
#output : error

#opening a file which does not exist
f = open('/Users/mehulgupta/Documents/Python/new_file.txt','w')
f.write('Hello')
f.close()
#output : A new file is created

#updating a file with new data(write mode overwrites new data in existing file)
f = open('/Users/mehulgupta/Documents/Python/records.txt','a')
text = 'hello'
f.write(text)
f.write(' mehul')
f.close()

#trying to write list in file
f = open('/Users/mehulgupta/Documents/Python/records.txt','w')
text_list = [1,2,3,4,5]
f.write(text_list)
f.close()
#output : error - only string values can be written

#another way of using file handling
with open('/Users/mehulgupta/Documents/Python/records.txt','r') as f:
    first_line = f.readline()
    print(first_line)

#using f.seek and f.tell
with open('/Users/mehulgupta/Documents/Python/records.txt','r') as f:
    print(f.tell())         #tells current position of cursor
    f.seek(4)               #you can position the cursor () bracket contains bytes
    print(f.tell())