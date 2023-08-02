#3) Fazer um programa que pergunte um valor em Dólares e apresente o equivalente em Reais. Considere U$1,00 = R$3,80.

dol = float(input("Digite um valor em dólar (U$) que converterei para você em real (R$): "))

real = dol * 3.80

print("O valor de U$", dol, "em reais é de R$", real)