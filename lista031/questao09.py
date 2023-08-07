#9) Fazer um algoritmo que pergunte 1 número e apresente:
#a) O próprio número
#b) O quadrado deste número
#c) A raiz quadrada deste número
import math

num = float(input("Digite um número que lhe direi o quadrado desse número e sua raíz quadrada: "))

pot = math.pow(num,2)

raiz = math.sqrt(num)

print("O número", num, "quando elevado ao quadrado é", pot, ". E a sua raíz é", raiz)
