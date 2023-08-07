
#10) Fazer um algoritmo que efetue o cálculo do valor de uma prestação em atraso, utilizando a fórmula prestação = valor + (valor x	(taxa : 100) x tempo em	dias)

print("Me informe o valor da prestação, a taxa da prestação e a quantos dias a prestação está atrasada")

val = float(input("Digite o valor da prestação: "))
taxa = float(input("Me informe a porcentagem da taxa de prestação: "))
dia = float(input("Me informe os dias de atraso da prestação: "))

pres = val + (val * (taxa / 100) * dia)

print("O valor da prestação que você deverá pagar no total é de:", pres)
