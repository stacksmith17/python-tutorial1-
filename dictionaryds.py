# dictionary 
d = {}


# in dictionary we have the pair of the values that is we have the key for which the values are stored in it 
d = {10:100,20:200,30:300,40:400}
print (d [10])
# we can create many keys and stores the value inside it as many as we want 
# we can change the pair in the values and keys both at the same time 
# we can the values of the key but we can't change the value of the key 

# operations in the dictionary can be performed as well 
d[10] =1000 # updating 
d[50] = 500 # creating 
del d[30] # removing the key and value both from the dictionary 



print (d)

# traversing in the dictionary
for i in d:
    print (i) # this will print the keys 

for i in d.values():
    print (i) # this will print the values in the keys 

for i in d :
    print (d[i])


help(dict)