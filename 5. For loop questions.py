a = int(input("Enter a number"))                             #pattern of 122333 in diff lines
b = 0
for x in range(a+1):
    for y in range(x):
        print(b,end="")
    print("\n")
    b +=1


alphabet = 65                                                #pattern of ABBCCC in diff lines
for x in range(1,5):
    for y in range(x):
        print(chr(alphabet),end="")
    alphabet += 1
    print("\n")



alphabet = 65                                                #pattern of ABCDE in diff lines
for x in range(5):
    for y in range(x):
        print(chr(alphabet),end="")                            
        alphabet += 1
    print("\n")


a = int(input("Enter a number"))                             #factorial of a number
fact = a
for  x in range(1,a):
    fact = fact*x
print(fact)

a = 0                                                        #fibonacci series
b = 1
print(a,",",b)
for x in range(2,21):
    c = a + b
    print(c, end = ",")

    a = b
    b =c 
