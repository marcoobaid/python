# Rewrite the program that prompts the user for a list of numbers and prints out 
# the maximum and minimum of the numbers at the end when the user enters “done”. 
# Write the program to store the numbers the user enters in a list and use the max()
# and min() functions to compute the maximum and minimum numbers 
# after the loop completes.

# Enter a number: 6
# Enter a number: 2
# Enter a number: 9
# Enter a number: 3
# Enter a number: 5
# Enter a number: done
# Maximum: 9.0
# Minimum: 2.0

t = []
maxi = 0
mini = 0
x = ""

while x != "done":
    try: # Ensure only numbers are used
        x = input("Enter a number: ")
        x = int(x)
        #count = count +1
        #total = total + x
        t.append(x)
        maxi = float(max(t))
        mini = float(min(t))
        
    except: # Excute for non-number input, or exit
        if x == "done":
            break   # break loop
        print('Invalid input. Type "done" to exit')
        continue

print('Maximum: ', maxi)
print('Minimum: ', mini)
#print('You have entered: ', t)
