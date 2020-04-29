salario = float(input('Qual o salario do funcionário?R$:'))
novosalario = salario + (salario *15/100)
print('O salario do funcionario de {:.2f} com 15° de aumento será {:.2f}.'.format(salario, novosalario))