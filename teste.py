from rich import print
from util import (
    pause,
    ler_float,
    ler_int
)
from logica import verificacao_nota

def cadastro_aluno(alunos):
    while True:

        # cadastro do nome
        nome = input("\nDigite o nome do aluno: ").strip().title()

        if not nome:
            print("Digite algum nome.")
            pause()
            continue

        if nome in alunos:
            print("Aluno já cadastrado.")
        else:
            break


    # cadastro da idade
    idade = ler_int("\nDigite a idade do aluno: ")

    # cadastro do email
    while True:
        email = input("\nDigite o email do aluno: ").strip()

    while True:
        qtde_notas = ler_int("\nDigite quantas notas o aluno possui: ")
        if qtde_notas > 0:
                break
        else:
            print("\nDigite um valor maior que 0.")
            pause()

    notas_validas = 0
    notas = []

    while notas_validas < qtde_notas:
        nota = ler_float("\nDigite uma nota do usuário: ")
        if verificacao_nota(nota):
            notas.append(nota)
            notas_validas += 1
        else:
            print("\nPor favor, digite um valor válido! (Nota entre 0 e 10)")
            pause()

    alunos[nome] = notas

cadastro_aluno({})