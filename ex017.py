D = int(input('Por quantos dias você alugou o carro?'))
km = float(input('Quantos Km percorreu com ele?'))
pago = (D * 60) + (km * 0.15)
print('O preço a pagar pelo veiculo é igual a R${:.2f}:'.format(pago))