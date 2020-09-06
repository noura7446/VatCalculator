

#vat calculator
vat=float(input("VAT without %:"))
price=float(input('Enter Amount:'))

total= price * vat/100
print("VAT added",total)
print("Gross Amount: ",total+price)
