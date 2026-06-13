x = int(input("Enter the number: "))
while(x % 5 != 0 and x % 10 != 0):
    x = int(input())
print(x)

#this loop terminates if the input is not multiple of 5 or 10 