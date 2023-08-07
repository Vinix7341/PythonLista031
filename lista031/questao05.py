#5) Fazer um programa que pergunte o salário de um funcionário e apresente este salário com um aumento de 15%.

sal = float(input("Me diga o seu salário e lhe direi quanto seria ele se fosse 15% mais alto: "))

val = sal + sal / 100 * 15

print("O valor do seu salário se tivesse um aumento de 15% seria de", val)