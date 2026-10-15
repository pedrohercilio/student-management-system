from rich import print
from menus import menuPrincipal
from opcoes import opcoes
from cadastro import cadastro_aluno, ler_json, salvar_json
from util import (
    recebe_escolha,
    pause
)

if __name__ == "__main__":
    alunos = ler_json()

    if alunos is None:
        raise SystemExit

    while True:
        menuPrincipal()

        escolha = recebe_escolha()

        if escolha is None:
            continue


        if escolha == 1:
            cadastro_aluno(alunos)

        elif escolha == 2:
            opcoes(alunos)

        elif escolha == 0:
            salvar_json(alunos)
            print("\nFim do programa...")
            break

        else:
            print("\nEscolha uma das opções.")
            pause()