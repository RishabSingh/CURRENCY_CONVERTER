with open ('exchangerates.txt') as f:
    lines=f.readlines()
currencyDict={}
for line in lines:
    parsed=line.split("\t")
    currencyDict[parsed[0]]=parsed[1]

amount=int(input('Enter Amount: \n'))
print('Enter the the name of the currency you want to convert this amount into? Available Options: \n')
[print(item) for item in currencyDict.keys()]
currency=input('Please enter one of these values: \n')
print(f'{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}')
