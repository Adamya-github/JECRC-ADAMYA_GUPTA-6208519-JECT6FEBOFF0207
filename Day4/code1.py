units=int(input("Enter units:"))
amount=0

if units>0:
    if units<=100:
        amount=units*5
    elif units<=300:
        amount=100*5 + (units-100)*7
    else:
        amount=100*5 + 200*7 + (units-300)*10
else:
    print("Invalid units")

if amount>5000:
    amount-=amount*0.05

print(amount)