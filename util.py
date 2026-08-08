from rich import print

def pause():
    input("Press enter to continue.")

def recebe_escolha():
    try:
        return int(input("\n"))
    except ValueError:
        print("\nPor favor, digite um valor válido!")
        pause()
        return None

def escolher_aluno(alunos):
    alunos_ordenados = sorted(alunos)
    numero_selecionado = None
    nome_selecionado = None

    print("\nAlunos cadastrados")
    for ordem, aluno in enumerate(alunos_ordenados, start= 1):
        print(f"{ordem} - {aluno}")


    aluno_selecionado = input("\nEscolha o aluno: ")
    try:
        numero_selecionado = int(aluno_selecionado)
    except ValueError:
        nome_selecionado = aluno_selecionado.strip().title()

    if numero_selecionado is not None and 1 <= numero_selecionado <= len(alunos_ordenados):
        nome_selecionado = alunos_ordenados[numero_selecionado - 1]

    if nome_selecionado in alunos:
        return nome_selecionado
    else:
        return None

def ler_int(frase):
    while True:
        try:
            return int(input(frase))
        except ValueError:
            print("\nPor favor, digite um valor válido.")
            pause()

def ler_float(frase):
    while True:
        try:
            return float(input(frase))
        except ValueError:
            print("\nPor favor, digite um valor válido.")
            pause()

def escolher_nota(nota_selecionada, quantidade_notas):
    numero_selecionado = None
    nota_selecionada = nota_selecionada.strip().title()
    try:
        numero_selecionado = int(nota_selecionada)
    except ValueError:
        if nota_selecionada.startswith("Nota"):
            try:
                numero_selecionado = int(nota_selecionada.split()[1])
            except (IndexError, ValueError): 
                pass
        if numero_selecionado is None:
            for i in range(quantidade_notas):
                if nota_selecionada == f"Nota {i + 1}":
                    numero_selecionado = i + 1
    return numero_selecionado