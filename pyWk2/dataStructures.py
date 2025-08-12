#Create new list
my_list=[]

#my_list += [10 ,20, 30, 40]

#Append values
y=10
for x in range(4):
    my_list.append(y)
    y=y+10
print(my_list)

#Insert a new value
my_list.insert(1, 15)


#Extend the list
my_list.extend([50, 60, 70])
print(my_list)

#Remove the last value
my_list.pop()
print(my_list)

#Sort in ascending order
my_list.sort()
print(my_list)

#Find and print the index of 30
index=my_list.index(30)
print(f"The index of 30 is {index}")