# list 
# syntax for creating the list 


a = [35,80,60,50,52]
# list can store any types of data inside it 

# aceesing of elements in list 
print (a[-1])

print (a[0:2])
# way of using the index 1st 

for i in range (len(a)):
    print (a[i])

# 2nd way of using directly 
for i in a :
    print (i)


# for adding the element in the last of the list is the append function is used 
a.append (40)

print (a)

# for inserting the element at the specific index we use the insert(index,data to inserted)
a.insert (1,15)
print (a)
# adding the multiple elements at the last of the elements we use the extend function 
a.extend ([45,50,55,60])
print (a)

# remove function is used to remove the element and its first appearance 

a.remove(15)
print (a)

# pop elemnt is used at the list to remove the element at the specifc position 


a.pop(3)
print (a )

# for finding the element at the specific index 

b = a.index(52)
print(b)

# count is used to count the occurence of the number 

c = a.count(50)
print (c) 

# sorting the list in ascending order 
a.sort ()
print (a)

# to reverse the order in the list we use the list function 
a.reverse ()
print (a)

# to create a copy of the list we use the copy function 

d = a.copy()
print (d)

# to clear all the elements of the list we use the clear function 
a.clear()
print(a)