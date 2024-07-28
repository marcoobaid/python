# Intialize variables
total = 0
count = 0
maxi = 0
mini = 0
x = None

# Calculate smallest value
def smallest(a,b): # compare new input "a" to current smallest "b"
    if a > b:
        return b
    else:
        return a

# Calculate largest value
def largest(a,b):
    if a < b:  # compare new input "a" to current largest "b"
        return b
    else:
        return a

# Enter loop
while x != "done":
    try: # Ensure only integers are used
        x = input("Enter a number: ")
        x = int(x)
        count = count +1
        total = total + x
        
        if count == 1:
            maxi = x
            mini = x
        else:
            maxi = largest(x,maxi)
            mini = smallest(x,mini)
            
    except: # Excute when non-integer input
        if x == "done":
            break   # break loop
        print("Invalid input")

print(total, count, maxi, mini)

