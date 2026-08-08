from rich import print
from util import (
    pause,
    recebe_escolha,
    escolher_aluno
)
import menus as m
import logica as l

def opcoes(alunos):
    if alunos:
        while True:
            m.menuOpcoes()

            escolha = recebe_escolha()

            if escolha is None:
                continue

            if escolha == 1:
                opcao_alunos(alunos)

            elif escolha == 2:
                opcao_turma(alunos)

            elif escolha == 3:
                opcao_ranking(alunos)

            elif escolha == 4:
                opcao_gerenciarAlunos(alunos)

            elif escolha == 0:
                break

            else:
                print("\nEscolha uma das opções.")
                pause()
    else:
        print("\nVocê ainda não cadastrou nenhum aluno.")
        pause()

def opcao_alunos(alunos):
    while True:
        m.menuAlunos()

        escolha = recebe_escolha()

        if escolha is None:
            continue

        if escolha == 1:
            opcao_alunosCadastrados(alunos)

        elif escolha == 2:
            opcao_alunoEspecifico(alunos)

        elif escolha == 3:
            opcao_melhorAluno(alunos)

        elif escolha == 4:
            opcao_piorAluno(alunos)

        elif escolha == 5:
            opcao_alunoConsistente(alunos)

        elif escolha == 6:
            opcao_alunoIrregular(alunos)

        elif escolha == 0:
            break

        else:
            print("\nEscolha uma das opções.")
            pause()

def opcao_alunosCadastrados(alunos):
    print("\nAlunos cadastrados:")
    for aluno in sorted(alunos):
        print("-", aluno)
    pause()

def opcao_alunoEspecifico(alunos):
    print("\nSituação e média de determinado aluno:")

    while True:
        nome_selecionado = escolher_aluno(alunos)

        if nome_selecionado is not None and nome_selecionado in alunos:
            situacao, media = l.situacao_aluno(alunos[nome_selecionado])
            print(f"\n{nome_selecionado} está {situacao} com média de {media:.2f} pontos.")
            pause()
            break

        else:
            print("\nPor favor, selecione algum aluno válido!")
            pause()

def opcao_melhorAluno(alunos):
    melhor_aluno, media = l.aluno_melhor(alunos)
    if len(melhor_aluno) == 1:
        print(f"\nO melhor aluno é {melhor_aluno[0]} com a média de {media:.2f} pontos.")
    elif len(melhor_aluno) > 1:
        print(f"\nOs melhores alunos são: {', '.join(melhor_aluno)} com a média de {media:.2f} pontos")
    pause()

def opcao_piorAluno(alunos):
    pior_aluno, media = l.aluno_pior(alunos)
    if len(pior_aluno) == 1:
        print(f"\nO pior aluno é {pior_aluno[0]} com a média de {media:.2f} pontos.")
    elif len(pior_aluno) > 1:
        print(f"\nOs piores alunos são: {', '.join(pior_aluno)} com a média de {media:.2f} pontos")
    pause()

def opcao_alunoConsistente(alunos):
    consistente, consistencia = l.aluno_consistente(alunos)
    if len(consistente) == 1:
        print(f"O aluno mais consistente é {consistente[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais consistentes são: {', '.join(consistente)} com a diferença de {consistencia:.2f} pontos entre as notas.")
    pause()

def opcao_alunoIrregular(alunos):
    irregular, consistencia = l.aluno_irregular(alunos)
    if len(irregular) == 1:
        print(f"O aluno mais irregular é {irregular[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais irregulares são: {', '.join(irregular)} com a diferença de {consistencia:.2f} pontos entre as notas.")
    pause()


def opcao_turma(alunos):
    while True:
        m.menuTurma()

        escolha = recebe_escolha()

        if escolha is None:
            continue

        if escolha == 1:
            opcao_mediaMedias(alunos)

        elif escolha == 2:
            opcao_mediaNotas(alunos)

        elif escolha == 3:
            opcao_distribuicaoNotas(alunos)

        elif escolha == 4:
            opcao_aprovados(alunos)

        elif escolha == 0:
            break

        else:
            print("\nEscolha uma das opcções.")
            pause()

def opcao_mediaMedias(alunos):
    media_da_turma = l.media_turma_medias(alunos)
    print(f"\nMédia das notas da turma: {media_da_turma:.2f}")
    pause()

def opcao_mediaNotas(alunos):
    media_da_turma = l.media_turma_notas(alunos)
    print(f"\nMédia das notas da turma: {media_da_turma:.2f}")
    pause()

def opcao_distribuicaoNotas(alunos):
    n10, n8, n6, n4, n2 = l.qtde_de_notas(alunos)
    print(f"\nNotas tiradas entre 8 e 10: {n10};\nNotas tiradas entre 6 e 8: {n8};\nNotas tiradas entre 4 e 6: {n6};\nNotas tiradas entre 2 e 4: {n4};\nNotas tiradas entre 0 e 2: {n2}")
    pause()

def opcao_aprovados(alunos):
    aprovados, em_recuperacao, reprovados = l.qtde_aprovacao(alunos)
    print(f"\nAprovados: {aprovados}\nReprovados: {reprovados}\nEm Recuperação: {em_recuperacao}")
    pause()



def opcao_ranking(alunos):
    while True:
        m.menuRanking()

        escolha = recebe_escolha()

        if escolha is None:
            continue

        if escolha == 1:
            opcao_rankingTurma(alunos)

        elif escolha == 2:
            opcao_top3(alunos)

        elif escolha == 0:
            break

        else:
            print("Escolha uma das opções.")
            pause()

def opcao_rankingTurma(alunos):
    print(f"\nRanking da turma:")
    for ordem, (aluno, notas) in enumerate(l.ranking_alunos(alunos), start=1):
        media = l.calcular_media(notas)
        print(f"{ordem}º - {aluno}, Média: {media:.2f}")

    pause()

def opcao_top3(alunos):
    print("\nTop 3 alunos:")
    for ordem, (aluno, notas) in enumerate(l.ranking_alunos(alunos), start=1):
        media = l.calcular_media(notas)
        if ordem <= 3:
            print(f"{ordem}º - {aluno}, Média: {media:.2f}")
    pause()

def opcao_gerenciarAlunos(alunos):
    while True:
        m.menuGerenciarAlunos()

        escolha = recebe_escolha()

        if escolha is None:
            continue

        if escolha == 1:
            opcao_infoAlunos(alunos)

        elif escolha == 2:
            opcao_editarAluno(alunos)

        elif escolha == 3:
            opcao_excluirAluno(alunos)

        elif escolha == 0:
            break

        else:
            print("\nEscolha uma das opções.")
            pause()

def opcao_infoAlunos(alunos):
    print("\n--- Informações dos alunos ---")
    alunos_ordenados = sorted(alunos)

    for aluno in alunos_ordenados:
        qtde_notas = len(alunos[aluno])
        notas = alunos[aluno]
        media = l.calcular_media(notas)

        print(f"\nNome: {aluno} -- Qtde de notas: {qtde_notas} -- Notas: {notas} -- Média: {media:.2f}")

    pause()

def opcao_editarAluno(alunos):
    while True:
        print("\nEditar informações de determinado aluno:")

        nome_selecionado = escolher_aluno(alunos)

        if nome_selecionado is not None and nome_selecionado in alunos:
            while True:

                qtde_notas = len(alunos[nome_selecionado])
                notas = alunos[nome_selecionado]
                media = l.calcular_media(notas)

                print("\nInformações do aluno:")
                print(f"Nome: {nome_selecionado}")
                print(f"Quantidade de notas: {qtde_notas}")
                print(f"Notas: {notas}")
                print(f"Média: {media:.2f}")

                print(f"\nQual informação de {nome_selecionado} você quer alterar?")
                print("1 - Nome")
                print("2 - Quantidade de Notas")
                print("3 - Alguma Nota")
                print("4 - Escolher outro aluno")
                print("0 - Sair sem editar")

                escolha = recebe_escolha()

                if escolha is None:
                    continue

                if escolha == 1:
                    l.editar_nome(alunos, nome_selecionado)
                    break

                elif escolha == 2:
                    l.editar_quantidadeNotas(qtde_notas, notas, nome_selecionado)
                    break

                elif escolha == 3:
                    l.editar_nota(qtde_notas, notas)
                    break

                elif escolha == 4:
                    break

                elif escolha == 0:
                    break

                else:
                    print("\nPor favor, selecione uma opção válida.")
                    pause()

            if escolha != 4:
                break

        else:
            print("\nPor favor, selecione algum aluno válido!")
            pause()

def opcao_excluirAluno(alunos):
    while True:
        print("\n=== Exclusão de Alunos ===")
        aluno_escolhido = escolher_aluno(alunos)
        if aluno_escolhido is not None and aluno_escolhido in alunos:
            while True:
                escolha = input(f"\nTem certeza que deseja excluir {aluno_escolhido} da lista? (y/n) ").capitalize()
                if escolha == 'Y':
                    alunos.pop(aluno_escolhido)
                    print(f"\nAluno excluído com sucesso!")
                    break
                elif escolha == 'N':
                    break
                else:
                    print("\nPor favor, digite apenas 'y' ou 'n'.")
                    pause()
            break
        else:
            print("Por favor, selecione um aluno válido.")
            pause()
