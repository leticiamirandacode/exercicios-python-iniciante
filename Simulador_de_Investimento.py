valor_investido = float(input("Valor a investir: R$ "))
meses = int(input("Tempo do investimento (meses): "))

if meses < 6:
    taxa = 0.005
elif 6 <= meses <= 12:
    taxa = 0.008
else:
    taxa = 0.012

if valor_investido > 10000:
    taxa += 0.001

rendimento_mensal = valor_investido * taxa
total = valor_investido + (rendimento_mensal * meses)

print(f"Taxa final aplicada: {taxa*100:.2f}% am")
print(f"Rendimento mensal: R$ {rendimento_mensal:.2f}")
print(f"Valor total após {meses} meses: R$ {total:.2f}")