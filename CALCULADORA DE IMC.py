# Programa para calcular o IMC
# Desenvolvido por Gabriel Ferreira

print("********************************************")
print("*         CALCULADORA DE IMC               *")
print("********************************************")
print()


# Criação das variáveis
Nome = ""
Peso = 0
Altura = 0.0
Imc = 0.0
# Entrada dos dados.
Nome = input("Digite  seu Nome: ")
Peso = int(input("Digite seu Peso: "))
Altura = float(input("Digite sua Altura: "))

# Processar valores para obter o IMC
Imc = Peso / Altura**2

#Saida do processamento
print()

print ("****************************")
print ("*       RESULTADO          *")
print ("****************************")
print ("*                          *")
print ("NOME: " + Nome)
print ("PESO: " + str(Peso) + "kg")
print ("ALTURA: " + str(Altura) + "m")
print ("IMC: " + str(Imc))
