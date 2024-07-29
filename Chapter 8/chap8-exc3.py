# Rewrite the guardian code in the Excercise 2 without two if statements. 
# Instead, use a compound logical expression using the or logical operator with a
# single if statement.

fhand = open('mbox-short-new.txt')

for line in fhand:
    words = line.split()
    # print('Debug:', words)
    if len(words) == 0 or words[0] != 'From' : continue
    
    # a guard for lines that start with From but are less that 3 words
    try:
        print(words[2])
    except:
        continue
