file = open("Week-8\concepts\working in read mode\example.txt", "r")
first_line = file.readline() # readline() method reads a line from a file and returns it as a string.
print(first_line.strip())  # to get rid of that extra '\n' character strip() method is used

second_line = file.readline()
print(second_line.strip())


print(file.readline())   # we can print directly without storing it     


file.close()