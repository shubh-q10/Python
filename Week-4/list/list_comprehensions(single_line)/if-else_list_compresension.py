l1 = [1, 2, 3, 4, 5]
l2 = [ l1[i]**2 if i%2 == 0 else l1[i]*2 for i in range(len(l1))] #squaring the num at the even index and multiplying with 2 at odd index
print(l2)

