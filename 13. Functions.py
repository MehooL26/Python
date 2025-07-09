def add_sum(x,y):                           #def add_sum(x=8,y=5) giving default values to the function
    added_value = x+y
    print(f'The sum is {added_value}')
    return added_value                     #returning the added value to the function, so this will be the output when the function is called

a=2
b=3
return_value = add_sum(a,b)                 #assigning our values to the function. These are positional arguments
print(return_value)

#(2,3,z=8)      z is a keyword argument, positional arguments cannot be written after keyword arguments



#in order to create a calculator, the user might want to add numerous digits and not only 2 so we use *args here
def calc(*args):
    sum_value = 0
    for x in args:
        sum_value += x
        print(f'value of x is{x}')
        print(f'added value is {sum_value}')
    return sum_value

a = 2
b = 3
c = 3
return_val = add_sum(a,b,c,10,35)
print(return_val)

# **kwargs collects the key word arguments

''' 
doc string can be written as """ doc string"""

it is printed as print(add_sum.__doc__)
'''