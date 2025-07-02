temp = input("Enter the temperature today")      #whenever we take a value from the user, it has a string type so we have to convert it
print(type(temp))
temp = int(input("Enter the temperature today"))
if temp > 45:
    print("weather is too hot")
elif 30<temp<45:
    print("weather is normal")
else : 
    print("The weather is good")