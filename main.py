'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
#vat calculator
vat=input("VAT without %:")
vat=float(vat)
price=input('Enter Amount:')
price=float(price)

total= price * vat/100
print("VAT added",total)
print("Gross Amount: ",total+price)
