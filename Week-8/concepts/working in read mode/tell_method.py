
#Purpose: Returns the current position of the file pointer (in bytes).

f = open("Week-8\concepts\working in read mode\example.txt", "r")
print(f.tell())      # At the beginning → 0
f.read(5)            # Read first 5 characters
print(f.tell())      # Now pointer moved → 5
f.close()
