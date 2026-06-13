

#WE CAN OPEN A FILE IN DIFFERENT MODES

# r - open an existing file for a read operation. If the file does not exist, it will throw an error.

# w - open an existing file for a write operation. If the file already contains some data, then it will 
      # be overridden but if the file is not present then it creates the file as well.

# a - open an existing file for append operation. It won’t override existing data. 
      # If the file is not present then it creates the file.
      
# r+ - To read and write data into the file. This mode does not override the existing data, 
      # but you can modify the data starting from the beginning of the file.

# w+ - To write and read data. It overwrites the previous file if one exists, 
      # it will truncate the file to zero length or create a file if it does not exist.
      
# a+ - To append and read data from the file. It won’t override existing data.


file = open("Week-8\concepts\working in read mode\example.txt", "r")

for line in file:
    print(line)
    
file.close()

