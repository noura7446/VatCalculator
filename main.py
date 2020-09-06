

#vat calculator
vat=input("VAT without %:")
vat=float(vat)
price=input('Enter Amount:')
price=float(price)

total= price * vat/100
print("VAT added",total)
print("Gross Amount: ",total+price)
