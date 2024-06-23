hrs = input('Enter Hours: ')
rte = input('Enter Rate: ')

# Compute Pay
def computepay(x,y):
    if x > 40:
        othrs = x - 40    # calculat overtime hours 
        otpay = y * 1.5   # calculate pay for the overtime hours
        pay = (40 * y) + (othrs * otpay )
    else:
        pay = x * y
    #print(pay)
    return pay

try: 
    hrs = float(hrs)
    rte = float(rte)
    pay = computepay(hrs,rte)    
    print(pay)    

except:
    print("Please enter a numeric input")
