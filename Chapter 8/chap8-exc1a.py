# Write a function called chop that takes a list and modifies it, 
# removing the first and last elements, and returns None. 
# Then write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements

def chop(lst):
    """
    Modifies the list by removing the first and last elements.
    Returns None.
    """
    if len(lst) > 1:
        del lst[0]
        del lst[-1]
    elif len(lst) == 1:
        lst.pop()
    else:
        print('This is an empty list')
    return None

# Example usage:
my_list = [1, 2, 3, 4, 5]
#my_list = [1]
#my_list = []

chop(my_list)
print(my_list)  # Output: [2, 3, 4]
