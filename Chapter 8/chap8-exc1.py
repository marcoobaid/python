# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements

def chop(x):
    length = len(x)
    for i in range(length):
        #print(x[i])
        if i == 0 or i == length - 2:
           #print(x[i])
           del x[i]
    print(x)

t = ['first', 'second', 'third', 'fourth', 'last']
chop(t)
