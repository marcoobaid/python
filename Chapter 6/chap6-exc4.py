str = 'X-DSPAM-Confidence: 0.8475'
atpos = str.find(' ') + 1
extract = float(str[atpos:])
#print(atpos)
print(extract)

