# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# 
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements

def middle(x):
    return x[1:-1]

t = ['first', 'second', 'third', 'fourth', 'last']

newlist = middle(t)

print('Original list: ', t)
print('Returned List: ', newlist)

