# there are two types of loop in the python language for and while loop 
# for loop is used for the numbers meanwhile while loop is used for the condition checking 


# for loop 
a = range (1,20,1) # it has three step in it (s,s,s) start stop and step 

for i in a :
    print (i)

# program to print the table of any number
n = int (input("which table we want to print ?"))

for i in range (n, (n*10)+1, n ):
    print(i)
# length of a string is calculated by len()


# break 
for i in range(1,21):
    if i==15:
        break # we can also use continue in place break to continue 
    else:
        print(i)