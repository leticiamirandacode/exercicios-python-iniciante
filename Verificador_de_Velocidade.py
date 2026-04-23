velocidade = float(input("Velocidade do veículo (km/h): "))
escola = input("É área escolar? (s/n): ").lower() == 's'
chuva = input("Está chovendo? (s/n): ").lower() == 's'

limite = 60 if chuva else 80

if velocidade > limite:
    excesso = velocidade - limite
    multa = excesso * 7

    if escola:
        multa *= 2

    print(f"MULTADO! Velocidade acima do limite de {limite}km/h.")
    print(f"Valor da multa: R$ {multa:.2f}")
else:
    print("Dentro do limite de velocidade. Boa viagem!")