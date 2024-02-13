# Printing numbers and strings in list
marks = [85, 84, 77, "Maths"]
print(marks)
print(" ") 

# Printing individual marks using index
marks = [85, 84, 77]
print(marks[0])


# Index in python can be negative i.e if we write marks[-1] it would print the item that is present in the last of list
# Similarly marks[-2] will print the second last item present in the list
# incase of marks[-4] list index will be out of range
marks = [85, 84, 77]
print(marks[-1])
print(" ") 

# Printing sub list from the whole list
marks = [94, 84, 83, 77, 99, 86]
print(marks[0:2])                # Doesnot include last index 
print(marks[1:3])                # Doesnot include last index
print(" ") 


# Printing list using for loop
marks = [94, 84, 83, 77, 99, 86]
for i in marks:
    print(i)