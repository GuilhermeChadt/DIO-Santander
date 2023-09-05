#-------------- CONVERSÃO DE DADOS ---------------------
preço = 10
idade = 30
print(preço, idade)
texto = f"Preço: {preço} e Idade: {idade}"
print(texto)
#------------- CONVERTENDO PARA FLOAT ------------------
preço_float = float(preço)
idade_float = float(idade)
texto_float = f"Dados em float: Preço: {preço_float} - Idade: {idade_float}"
print(texto_float)
#------------- CONVERTENDO PARA INTEIRO -----------------
preço_int = int(preço_float)
idade_int = int(idade_float)
texto_int = f"Dados em int: Preço: {preço_int} Idade: {idade_int}"
print(texto_int)
#------------- CONVERTENDO PARA TUPLA ------------------
nome = "Marcio Fernandes Andrade"
nome_tuple = tuple(nome)
texto_tuple = f"Nome em tupla: {nome_tuple}"
print(texto_tuple)
#------------- CONVERTENDO PARA LISTA -------------------
# Usando variável 'nome' já definida em exemplo acima
nome_list = list(nome)
texto_list = f"Nome em lista: {nome_list}"
print(texto_list)

