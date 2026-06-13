n = int(input("Enter any number  "))
if (n<0):
    print("The number is invalid")
else:
    i = 1
    factorial = 1
    while(i <= n): #This will run until i is = or < than n 
        factorial = factorial*i
        i += 1
    print("Factorial of", n, "is:", factorial)