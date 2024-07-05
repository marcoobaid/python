# Intialize variables
total = 0
count = 0
average = 0
x = None

# Enter loop
while True:
    x = input("Enter a number: ")
    if x == "done":
            break   # break loop
    
    try: # Ensure only integers are used
        x = int(x)
        count = count +1
        total = total + x
        average = total / count

    except: # Excute when non-integer input
        print("Invalid input")
        continue

print(total, count, average)
