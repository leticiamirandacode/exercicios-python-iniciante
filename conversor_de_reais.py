real=float(input('Quantos dinheiro você tem na carteira? R$ '))
dolar= real / 5.2125
euro= real / 6.0764
print(f'Com R${real:.2f} você pode comprar U${dolar:.2f} e €{euro:.2f}')
