x = 5
#basic f-string formatting

print(f'The value of x is {x}')

#width formatting x:5d

print(f'The value of x is {x:5d}') #The number 5 is right-aligned, and extra spaces are added to fill the width.

#zero padding

print(f'The value of x is {x:05d}')#The number 5 is right-aligned, and extra spaces replaced with 0 to fill the width.

#right aligned with zero padding

print(f"The value of x is {x:>05d}")#same as x:o5d coz right aligned is default

#left aligned with zero padding

print(f'The value of x is {x:<05d}')#The number 5 is left-aligned, and extra spaces replaced with 0 ot fill the width.

#center aligned with zero padding

print(f'The value of x is {x:^07d}')#The number 5 is center-aligned, and extra spaces replaced with 0 to fill the width.

# Floating-point Formatting (x:.2f)

print(f'The value of x is {x:.2f}')#show 2 decimal places