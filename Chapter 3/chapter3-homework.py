# Ask for a score
x = input('Enter score: ')

# Evalute input and output score
try:
    x = float(x)
    if x >= 0.9 and x <= 1:
        print('A')
    elif x >= 0.8 and x < 0.9:
        print ('B')
    elif x >= 0.7 and x < 0.8:
        print ('C')
    elif x >= 0.6 and x < 0.7:
        print ('D')
    elif x >= 0 and x < 0.6:
        print ('F')
    else:
        print ('Bad Score')  # numbers not within 0 and 1 range are bad

except:
    print('Bad Score') # non-numberic input is bad
