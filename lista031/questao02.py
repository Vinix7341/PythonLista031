#2) Elaborar um programa que pergunte quatro valores inteiros e apresente 2 resultados:
#a) Resultado de suas adições
#b) Resultado de suas multiplicações

print("Me diga quatro números e lhe darei a soma dos quatro números e a multiplicação dos quatro números.")

v1 = float(input("Informe o primeiro número: "))
v2 = float(input("Informe o segundo número: "))
v3 = float(input("Informe o terceiro número: "))
v4 = float(input("Informe o quarto número: "))

soma = v1 + v2 + v3 + v4
mult = v1 * v2 * v3 * v4

print("A soma dos quatro números é", soma, "e a multiplicação dos quatro números é", mult)