# Sometimes when programmers get bored or want to have a bit of fun, 
# they add a harmless Easter Egg to their program. Modify the program 
# that prompts the user for the file name so that it prints a funny message
# when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t exist.
#  Here is a sample execution of the program:

# python egg.py
# Enter the file name: mbox.txt
# There were 1797 subject lines in mbox.txt
# 
# python egg.py
# Enter the file name: missing.tyxt
# File cannot be opened: missing.tyxt
# 
# python egg.py
# Enter the file name: na na boo boo
# NA NA BOO BOO TO YOU - You have been punk'd!

try:
    fname = input('Enter the file name: ')
    fhandle = open(fname)
    count = 0
    total = 0 
    for line in fhandle:
        line = line.rstrip()
        if line.startswith('X-DSPAM-Confidence: '):
            fpoint = float(line[20:])
            count = count + 1
            total = total + fpoint        
        # average = total/count  # OR
    print(f'Average spam confidence: {total/count}')
except:
    if fname == 'na na boo boo':
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
    else:
        print('File cannot be opened: ', fname)
    #quit()

