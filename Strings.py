data = "i am learning python"
print(data.upper())                         #upper case of all letters
print(data.lower())                         #lowercase of all letters
print(data.capitalize())                    #first letter is capitalized
print(data.title())                         #first letter of each word is capitalized
print(data.swapcase())                      #swaps uppercase to lowercase and vice versa

print(data.ljust(30,"*"))
print(data.rjust(30,"*"))
print(data.center(30,"*"))

print("length of data is:",len(data))       #to find length of variable

data = input("Enter the name")              #checking whether input data is string or not
print(data.isalpha())

print(data.startswith("data"))              #it is case sensitive
print(data.endswith("data"))


data_val = "India is a country"
print(len(data_val))

data_val = " India is a country "
print(len(data_val.strip(" ")))             #It removes the particular character

print(data_val.count("India"))              #Counts the number of times the string is present in the variable

print(data_val.partition(" "))

print(data_val.index("count"))              #Tells the postion of the string but gives error if string not present in the variable
print(data_val.find("count"))               #Performs the same task but gives output -1 if string is not present

print(data_val.split(" "))                  #Splits the string  

print(data_val.join("123"))
