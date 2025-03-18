hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
rateplus = input("Enter RatePlus:")
rp = float(rateplus)

if h > 40:
    print(r*40 + r*rp*(h-40))
else:
    print(r*h)