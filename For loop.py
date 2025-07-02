for y in range(5):
    print("value of y is:",y)                       #if the start and step are not specified then start is by default=0 and increment=1

    #the output will be -1 than the end nummber


for x in range(1,5,1):                              #(start,end,step)  step is the incrementation 
    print("value of x is:",x)



#going reverse for a number
data = 10                                           #assigning the value
for x in range(data,1,-2):
    print("value of x is",x)



#we can go in reverse order by using 'reversed(range())' also
data = int(input("Enter a number"))                 #getting a input from user and converting the data type
for x in reversed(range(10)):
    print("the value of x is:",x)

a = 1
for x in range(5):
    for y in range(x):
        print(a,end="")        #to print a statement in the same line
        a = a+1         
    print("\n")