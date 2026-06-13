#Here we are going to read a file and store all the lines in a list format.

file = open("Week-8\concepts\working in read mode\example.txt", "r")
l = file.readlines() # readlines() method reads all the lines of the file and
                     # returns in a list format where every line is an item of the list
print(l)
file.close()