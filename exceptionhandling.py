# errors in the program 
""" error are the mistake in the code that prevent it from running.  these can be two types of error it is syntax or logical

syntax error 
mistake in the syntax 
print ( hello world this will show the mistake due to closing of the bracket


identatiopn error ;
if x > 0:
print("Positive")
 this may create the mistake due to the space and all 
 the  correct code for it will be  
 if x > 0:
    print("Positive")

exceptions :
Exceptions are unexpected events or errors that occurs
during the execution of a program, which disrupts the normal
flow of the program.

"""
a = int (input("enter the number you want to divide 10 with :"))
try:
    print (10/a)

# this will be zerodivison when the 0 is given as the input 

# we use except to make the exception possible 
except ZeroDivisionError :
    print("sorry we can't divide by 0") # we can also use Exception as err if we dont know the name of the error 

else :#Run code only if no exception occurs
    print ("there is no exception ")

finally: #Run code no matter what, whether there’s an exception or not
    print ("i will run no matter what ")

print ("division is completed ")

# for exception of error we use the except and the actual where the exception is occuring that is wrapped in the try 

# another function raise can be used to create the manual error 


age = int (input ("tell your age :"))

if age <10 or age >18 :
    raise ValueError ("your age must be between 10 and 18 ")
else :
    print ("welcome playclub")
    