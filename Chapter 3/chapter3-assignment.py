hrs = input("Enter Hours: ")
h = float(hrs)
rte = input("Enter rate: ")
r = float(rte)

if h > 40:
    othrs = h - 40
    otrte = r * 1.5
    pay = (40 * r) + (othrs * otrte)
else:
    pay = h * r

print(pay)
