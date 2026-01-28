# sets is an unordered collection of unique elements 
# set is defined with {}

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# operation are all those we use in the mathematical sets 
# union of sets 
A|B
print (A|B) #or we can use the A.union(B)

#intersection of sets 
print (A&B) # or we can use the A.intersection(B)

#difference in sets 
print (A-B)

#Subset
print (A<=B)
# we can also use a.issuperset(b)

# disjoint 
A.isdisjoint(B)



# methods in the sets 
lst = [1, 2, 3]

# adding the elements in the 