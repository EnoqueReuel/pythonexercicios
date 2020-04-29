real = float(input('Quanto dinheiro você tem na carteira? R$:'))
dolar = real / 5.59
print('com R${:.2f} você pode comprar U$${:.2f}'.format(real, dolar))

real = float(input("How much money do you have? R$:"))
EURO = real / 6.05
print('with R${:.2f} you can buy EURO {:.2f}'.format(real, EURO))

real = float(input('How much money do you have?'))
LB = real / 6.92
print('with R${:.2f} you can buy Libra esterlina {:.2f}'.format(real, LB))

