
#8) Fazer um programa que calcule e apresente a quantidade de litros que um automóvel gastará em uma viagem. O programa deve coletar as seguintes informações: Distância a percorrer na viagem, em quilômetros; qual é o valor do consumo médio do automóvel, em quilômetros por litro

print("Me informe a distância da sua viagem em quilômetros e quantos litros o seu automóvel gasta por quilômetro que lhe direi seu gasto nessa viagem!")

dis = float(input("Digite quantos quilômetros será percorrido na viagem: "))

cons = float(input("Digite quantos litro o seu automóvel gasta por quilômetro percorrido: "))

gasto = cons * dis

print("O seu automóvel gastará na viagem um total de", gasto, "litros")