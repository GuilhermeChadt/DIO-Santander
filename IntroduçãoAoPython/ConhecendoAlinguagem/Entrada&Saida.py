#------------------------- Entrada de dados do usuário --------------------------------
nome = input("Digite seu primeiro nome:")
idade = input("Digite sua idade:")
#------------------------- Saída de dados do usuário ----------------------------------
print("Seu nome é: ", nome)
print("Sua idade é: ", idade)
#------------------------- Saída de dados do usuário com 'end' ------------------------
print("Seu nome é: ", nome, " E sua idade é: ", idade, "-", end = "FINISH DATA \n")
#------------------------- Saída de dados do usuário com 'sep' ------------------------
print("Seu nome é: ", nome, sep = "-->>")