name = input("Name: ")
course = input("Course: ")
with open("student.txt", "w") as file:
    file.write("Name: " + name + "\n")
    file.write("Course: " + course + "\n")
print("Information saved.")
