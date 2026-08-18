import json
def baran():
    print("\n\n")

# quatro principais comandos:

informacao = {
    "1 + 1 = ?": 2,
    "2 + 2 = ?": 4
}

# json.dumps() -> transforma um objeto python em uma string json
json_dumps = json.dumps(informacao)
print(json_dumps) # -> vira string
print(type(json_dumps))
baran()

# json.loads() -> recebe uma string json e transforma em uma estrutura python
texto = '{"py":"thon", "c": "++"}'
json_loads = json.loads(texto)
print(json_loads)
print(type(json_loads))
baran()

# json.load() -> lê arquivo
with open("lista.json", "r", encoding="utf-8") as arquivo:
    lista = json.load(arquivo)
print(lista)


# json.dump() -> salva em arquivo json
novo_dicionario = {"1": "tres", 4: 3}
with open("numeros_aleatorios.json", "w",
           encoding="utf-8" # -> Define como os caracteres são codificados no arquivo; dizer ao python: "Use UTF-8 para codificar os caracteres desse arquivo."
           ) as arquivo:
    json.dump(novo_dicionario,
            arquivo,
            indent=4, # -> quantidade de espaços para cada linha nova
            ensure_ascii=False # -> "Não transforme caracteres Unicode em escapes ASCII; mantenha os caracteres normalmente."
            )

# serialização -> transformar uma estrutura de dados em um formato que pode ser armazenado ou transmitido

# JSON também é um arquivo para armazenar configurações;
# Usado principalmente para representar e transportar dados estruturados





print("alunos.json".startswith("alunos")) # -> verifica se o começo de determinada str é igual ao indicado
print("alunos.json".endswith(".json")) # -> faz o inverso, verifica o final


texto = "Olá Pedro"

novo_texto = texto.replace("Pedro", "João") # -> substitui uma parte da string por outra

print(f"\n\n{novo_texto}")

# string.replace(alvo, substituto)