#Purpose: Moves the file pointer to a specific position.


f = open("Week-8\concepts\working in read mode\example.txt", "r")
f.read(5)            # Read first 5 chars
print(f.tell())      # Pointer at 5
f.seek(0)            # Move pointer back to start
print(f.read(5))     # Reads same 5 chars again
f.close()
