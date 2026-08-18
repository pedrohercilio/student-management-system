algo = input("Digite algo: ")
print(f"O tipo digitado é: {type(algo)}")
print(f"Só tem espaços? {algo.isspace()}") # True se só houver espaços
print(f"Só tem números? {algo.isnumeric()}") # True se só houver número
print(f"Só tem Letras? {algo.isalpha()}") # True se só letras (alfabeto)
print(f"É Alfanumérico123? {algo.isalnum()}") # True se AlfaNumérico
print(f"Só tem Maiúsculas? {algo.isupper()}") # True se só maiúsculas
print(f"Só tem Minúsculas? {algo.islower()}") # True se só minúsculas
print(f"Está capitalizada? {algo.istitle()}") #Tem maiúsculas e minúsculas
