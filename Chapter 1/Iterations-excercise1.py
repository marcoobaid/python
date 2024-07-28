# Intialize variables
total = 0
count = 0
average = 0
x = None

# Enter loop
while x != "done":
    x = input("Enter a number: ")

    try: # Ensure only integers are used
        x = int(x)
        count = count +1
        total = total + x
        average = total / count

    except: # Excute when non-integer input
        if x == "done":
            break   # break loop
        print("Invalid input")

print(total, count, average)
