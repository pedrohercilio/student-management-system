from rich import print
from util import (
    pause,
    ler_float,
    ler_int
)
from logica import (
    verificacao_nota,
    ler_json,
    salvar_json
)


def cadastrar_matricula(alunos, novo_aluno):
    maior = max(
        (int(aluno["_referencia"]) for aluno in alunos.values()),
        default=0
    )
    referencia = str(maior + 1)
    novo_aluno["_referencia"] = referencia
    novo_aluno["matricula"] = referencia.zfill(2)
    return referencia
        
def cadastrar_nome(alunos, novo_aluno):
    while True:

        nome = input("\nDigite o nome do aluno: ").strip().title()
        sobrenome = input("\nDigite o sobrenome do aluno: ").strip().title()
        nome_completo = nome + " " + sobrenome

        if not nome or not sobrenome:
            print("\nDigite algum nome.")
            pause()
            continue

        if nome_completo not in alunos:
            novo_aluno["nome"] = nome_completo
            break
        print("\nAluno já cadastrado.")
        pause()

def cadastrar_idade(novo_aluno):
    idade = ler_int("\nDigite a idade do aluno: ")
    if idade > 0:
        novo_aluno["idade"] = idade

def cadastrar_notas(novo_aluno):
    while True:
        quantidade_notas = ler_int("\nDigite quantas notas o aluno possui: ")
        if quantidade_notas > 0:
            break
        print("\nDigite um valor maior que 0.")
        pause()

    while len(novo_aluno["notas"]) < quantidade_notas:
        nota = ler_float("\nDigite uma nota do aluno: ")
        if verificacao_nota(nota):
            novo_aluno["notas"].append(nota)
        else:
            print("\nDigite uma nota válida entre 0 e 10.")
            pause()


def cadastro_aluno(alunos):
    novo_aluno = {"matricula": "",
                  "nome": "",
                  "idade": 0,
                  "notas": []
                 }

    cadastrar_matricula(alunos, novo_aluno)

    cadastrar_nome(alunos, novo_aluno)

    cadastrar_idade(novo_aluno)

    cadastrar_notas(novo_aluno)

    print("\nMatrícula, nome, idade e notas cadastrados com sucesso!\n")
    alunos[novo_aluno["nome"]] = novo_aluno