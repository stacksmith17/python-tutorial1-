#Tuples are a built-in data type in Python used to store a collection of items
# the major difference between them is that we can change the elements presenr in the list but in tuples we can't change it

l= (10,20,30,40,50)
# the list can be represented by the using paranthesis or without the paranthesis 

#acessing the element in the tuples by indexing 
print(l[0])
print(l[-1])


# slicing the tuples 
print (l[1:4])
print (l[:3])
print (l[::2])

# looping through the tuples 
for i in l :
    print (i)

# concatenation of tuples 
t1 = (1,2,3)
t2 = (4,5,6)
t3 = t1+t2 
print (t3)

# repetition in tuples 
t = (9,8)
print (t*3) #(9,8,9,8,9,8)


# checking the memebership in tuples 
print (20 in l)
print (9 in t)
print (10 in t)

# built in function in tuples 
print(len(t))   # length of the tuples 
print(max(t))   # max element in the tuples 
print(min(t))   # minimum element in the tuples 
print(sum(t))   #  print all elements in the tuples 

# tuples method (2 methods)
# count()
print (t.count(9)) # prints the number of elements present in tuples 

# index ()
print(l.index(20)) # prints the index number of the elements 



# conversion between list and tuples 
m = (4,5,6)
n = list (m) # this will convert the tuples to list 
n.append (7)
m = tuple (n)
print (m)
# we can't add the element to the tuples so we have to convert it to the list then we have to add element in it 

# tuples unpacking 
a,b,c,d,e = l
print (a)
print (b)
print (c)
print (d)
print (e)
