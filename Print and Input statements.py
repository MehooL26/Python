emp_name = "Mehul Gupta"                                #different types of print statements
emp_id  = 10
print("Name of employee is",emp_name,"and employee id is",emp_id)
print(f"Name of employee is {emp_name} and employee id is {emp_id}")
print("Name of employee is %s and employee id is %d" %(emp_name,emp_id))
print("Name of employee is {0} and employee id is {1}".format(emp_name,emp_id))         #stays in sequence
print("Name of employee is {0} and employee id is {1} and name of employee again {0}".format(emp_name,emp_id))  

name = input("Enter your name: ")                       #taking value from user
number = int(input("Enter a number"))                   #by default, class of variable of input is string so need to convert it to integer class to perform arithmetic operations
