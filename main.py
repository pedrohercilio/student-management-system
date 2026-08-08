from rich import print
from menus import menuPrincipal
from opcoes import opcoes
from logica import cadastro_aluno
from util import (
    recebe_escolha,
    pause
)

def main():
    alunos = {}

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
            print("\nFim do programa")
            break

        else:
            print("\nEscolha uma das opções.")
            pause()
if __name__ == "__main__":
    main()