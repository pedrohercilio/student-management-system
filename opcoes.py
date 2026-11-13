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
            lista_vazia = False
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
                lista_vazia = opcao_gerenciarAlunos(alunos, lista_vazia)
                if lista_vazia == True:
                    break

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
        matricula = alunos[aluno]["matricula"]
        idade = alunos[aluno]["idade"]
        print(f"- {aluno}, {idade} anos (Matrícula: {matricula})")
    pause()

def opcao_alunoEspecifico(alunos):
    print("\nSituação e média de determinado aluno:")

    while True:
        nome_selecionado = escolher_aluno(alunos)

        if nome_selecionado is not None and nome_selecionado in alunos:
            registro = alunos[nome_selecionado]
            situacao, media = l.situacao_aluno(registro["notas"])
            print(f"\n{nome_selecionado} está {situacao} com média de {media:.2f} pontos.")
            pause()
            break

        else:
            print("\nPor favor, selecione algum aluno válido!")
            pause()

def opcao_melhorAluno(alunos):
    melhor_aluno, media = l.aluno_melhor(alunos)
    alunos_com_matricula = [
        f"{aluno} (Matrícula: {alunos[aluno]['matricula']})"
        for aluno in melhor_aluno
    ]
    if len(melhor_aluno) == 1:
        print(f"\nO melhor aluno é {alunos_com_matricula[0]} com a média de {media:.2f} pontos.")
    elif len(melhor_aluno) > 1:
        print(f"\nOs melhores alunos são: {', '.join(alunos_com_matricula)} com a média de {media:.2f} pontos")
    pause()

def opcao_piorAluno(alunos):
    pior_aluno, media = l.aluno_pior(alunos)
    alunos_com_matricula = [
        f"{aluno} (Matrícula: {alunos[aluno]['matricula']})"
        for aluno in pior_aluno
    ]
    if len(pior_aluno) == 1:
        print(f"\nO pior aluno é {alunos_com_matricula[0]} com a média de {media:.2f} pontos.")
    elif len(pior_aluno) > 1:
        print(f"\nOs piores alunos são: {', '.join(alunos_com_matricula)} com a média de {media:.2f} pontos")
    pause()

def opcao_alunoConsistente(alunos):
    consistente, consistencia = l.aluno_consistente(alunos)
    alunos_com_matricula = [
        f"{aluno} (Matrícula: {alunos[aluno]['matricula']})"
        for aluno in consistente
    ]
    if len(consistente) == 1:
        print(f"O aluno mais consistente é {alunos_com_matricula[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais consistentes são: {', '.join(alunos_com_matricula)} com a diferença de {consistencia:.2f} pontos entre as notas.")
    pause()

def opcao_alunoIrregular(alunos):
    irregular, consistencia = l.aluno_irregular(alunos)
    alunos_com_matricula = [
        f"{aluno} (Matrícula: {alunos[aluno]['matricula']})"
        for aluno in irregular
    ]
    if len(irregular) == 1:
        print(f"O aluno mais irregular é {alunos_com_matricula[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais irregulares são: {', '.join(alunos_com_matricula)} com a diferença de {consistencia:.2f} pontos entre as notas.")
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
    for ordem, (aluno, registro) in enumerate(l.ranking_alunos(alunos), start=1):
        notas = registro["notas"]
        media = l.calcular_media(notas)
        print(f"{ordem}º - {aluno} (Matrícula: {registro['matricula']}), Média: {media:.2f}")

    pause()

def opcao_top3(alunos):
    print("\nTop 3 alunos:")
    for ordem, (aluno, registro) in enumerate(l.ranking_alunos(alunos), start=1):
        notas = registro["notas"]
        media = l.calcular_media(notas)
        if ordem <= 3:
            print(f"{ordem}º - {aluno} (Matrícula: {registro['matricula']}), Média: {media:.2f}")
    pause()

def opcao_gerenciarAlunos(alunos, lista_vazia):
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
            lista_vazia = opcao_excluirAluno(alunos, lista_vazia)
            return lista_vazia

        elif escolha == 0:
            break

        else:
            print("\nEscolha uma das opções.")
            pause()

def opcao_infoAlunos(alunos):
    print("\n--- Informações dos alunos ---")
    alunos_ordenados = sorted(alunos)

    for ordem, aluno in enumerate(alunos_ordenados, start=1):
        registro = alunos[aluno]
        notas = registro["notas"]
        qtde_notas = len(notas)
        media = l.calcular_media(notas)

        print(
            f"\n{ordem} - Nome: {aluno}"
            f"\nMatrícula: {registro['matricula']} "
            f"\nIdade: {registro['idade']}"
            f"\nQuantidade de notas: {qtde_notas}"
            f"\nNotas: {notas}"
            f"\nMédia: {media:.2f}"
        )

    pause()

def opcao_editarAluno(alunos):
    while True:
        print("\nEditar informações de determinado aluno:")

        nome_selecionado = escolher_aluno(alunos)

        if nome_selecionado is not None and nome_selecionado in alunos:
            while True:

                registro = alunos[nome_selecionado]
                notas = registro["notas"]
                qtde_notas = len(notas)
                media = l.calcular_media(notas)

                print("\nInformações do aluno:")
                print(f"Nome: {nome_selecionado}")
                print(f"Matrícula: {registro['matricula']}")
                print(f"Idade: {registro['idade']}")
                print(f"Quantidade de notas: {qtde_notas}")
                print(f"Notas: {notas}")
                print(f"Média: {media:.2f}")

                print(f"\nQual informação de {nome_selecionado} você quer alterar?")
                print("1 - Nome")
                print("2 - Quantidade de Notas")
                print("3 - Alguma Nota")
                print("4 - Idade")
                print("5 - Escolher outro aluno")
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
                    l.editar_idade(alunos, nome_selecionado)
                    break

                elif escolha == 5:
                    break

                elif escolha == 0:
                    break

                else:
                    print("\nPor favor, selecione uma opção válida.")
                    pause()

            if escolha != 5:
                break

        else:
            print("\nPor favor, selecione algum aluno válido!")
            pause()

def opcao_excluirAluno(alunos, lista_vazia):
    while True:
        print("\n=== Exclusão de Alunos ===")
        aluno_escolhido = escolher_aluno(alunos)
        if aluno_escolhido is not None and aluno_escolhido in alunos:
            registro = alunos[aluno_escolhido]
            print(f"\nNome: {aluno_escolhido}")
            print(f"Matrícula: {registro['matricula']}")
            print(f"Idade: {registro['idade']}")
            while True:
                escolha = input(f"\nTem certeza que deseja excluir {aluno_escolhido} da lista? (y/n) ").strip().upper()
                if escolha == 'Y':
                    alunos.pop(aluno_escolhido)
                    print(f"\nAluno excluído com sucesso!")
                    if not(alunos.keys()):
                        lista_vazia = True
                        return lista_vazia
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
