# Use of break
students = ["Uswa", "Aqsa", "Afeera", "Rafia", "Zanib"]

for i in students:
    if i == "Afeera":
        break
    print(i)
print(" ")

# Use of continue
students = ["Uswa", "Aqsa", "Afeera", "Rafia", "Zanib"]

for i in students:
    if i == "Afeera":          # Afeera will not get print
        continue
    print(i)