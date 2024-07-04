def largest(a,b):
    if a > b:
        return a
    else:
        return b
    
x = int(input("Enter first value: "))
y = int(input("Enter second value: "))



maximum = largest(x,y)

print(maximum)
