#lambda is used as a function for smaller operations 
a = 10
x = lambda a: a+10
print (x(a))


x = lambda a,b : a*b
print(x(10,20))


id = [100,103,107,110]
emp_id = filter(lambda x : x%2==1,id)             #filter(function,iterable)
print(emp_id)       #here we have to convert emp_id into a list else it will give address as output

emp_id = list(filter(lambda x : x%2==1,id))
print(emp_id)


A = [1,2,3,4,5]
B = ['m','n','o','p','q']
a = list(zip(A,B))                  #important to convert into list
print(a)