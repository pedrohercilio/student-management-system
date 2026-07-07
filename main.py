from rich import print

def verificacao_nota(nota):
    if 0 <= nota <= 10:
        return True
    else:
        return False #garante que retorne falso se for inválida
   
def calcular_media(notas):
    # Evita divisão por zero caso o aluno ainda não possua notas.
    if not notas:
        return 0
    return sum(notas)/len(notas)

def situacao_aluno(notas): 
    media = calcular_media(notas)

    if media >= 7:
        return "Aprovado",media
    elif 5<= media < 7:
        return "em Recuperação",media
    else:
        return "Reprovado",media
    
def media_turma_medias(alunos):
    if not alunos:
        return 0
    lista_notas = []
    for notas in alunos.values():
        media = calcular_media(notas)
        lista_notas.append(media)
    return sum(lista_notas)/len(lista_notas)

def media_turma_notas(alunos):
    soma_notas = 0
    len_notas = 0
    for notas in alunos.values():
        soma_notas = soma_notas + sum(notas)
        len_notas = len_notas + len(notas)

    if len_notas == 0:
        return 0
    return soma_notas/len_notas

def aluno_melhor(alunos): 

    maior_nota = float('-inf')
    # Garante que a primeira média encontrada seja armazenada.

    for aluno, notas in alunos.items():
        media = calcular_media(notas)

        if media > maior_nota:
            maior_nota = media
            melhoraluno = [aluno]

        # Em caso de empate, todos os alunos com a maior média são armazenados.
        elif media == maior_nota:
            melhoraluno.append(aluno)
    return melhoraluno, maior_nota

def aluno_pior(alunos): 

    menor_nota = float('inf')
    # Garante que a primeira média encontrada seja armazenada.

    for aluno, notas in alunos.items():
        media = calcular_media(notas)

        if media < menor_nota:
            menor_nota = media
            pioraluno = [aluno]

        # Em caso de empate, todos os alunos com a menor média são armazenados.
        elif media == menor_nota:
            pioraluno.append(aluno)
    return pioraluno, menor_nota

def qtde_aprovacao(alunos):
    aprovados = 0
    em_recuperacao = 0
    reprovados = 0
    for notas in alunos.values():
        aprovacao, media = situacao_aluno(notas)
        if aprovacao == "Aprovado":
            aprovados += 1
        elif aprovacao == "em Recuperação":
            em_recuperacao += 1
        elif aprovacao == "Reprovado":
            reprovados += 1
    return aprovados, em_recuperacao, reprovados

def qtde_de_notas(alunos): 
    n8_10 = 0
    n6_8 = 0
    n4_6 = 0
    n2_4 = 0
    n0_2 = 0
    for notas in alunos.values():
        for nota in notas:
            if 8 <= nota <= 10:
                n8_10 += 1
            elif 6 <= nota < 8:
                n6_8 += 1
            elif 4 <= nota < 6:
                n4_6 += 1
            elif 2 <= nota < 4:
                n2_4 += 1
            elif 0 <= nota < 2:
                n0_2 += 1
    return n8_10, n6_8, n4_6, n2_4, n0_2

def diferenca_notas(notas):
    if not notas:
        return 0
    return max(notas) - min(notas)

def aluno_consistente(alunos):
    consistencia = float("inf")
    aluno_ci = []
    for aluno, notas in alunos.items():
        diferenca = diferenca_notas(notas)

        if diferenca < consistencia:
            consistencia = diferenca
            aluno_ci = [aluno]

        # Em caso de empate, todos os alunos mais consistentes são armazenados.    
        elif diferenca == consistencia:
            aluno_ci.append(aluno)
    return aluno_ci, consistencia

def aluno_irregular(alunos):
    consistencia = float("-inf")
    aluno_ci = []
    for aluno, notas in alunos.items():
        diferenca = diferenca_notas(notas)

        if diferenca > consistencia:
            consistencia = diferenca
            aluno_ci = [aluno]
            
        # Em caso de empate, todos os alunos mais irregulares são armazenados.
        elif diferenca == consistencia:
            aluno_ci.append(aluno)
    return aluno_ci, consistencia

def pause():
    input("Press enter to continue.")

def ranking_alunos(alunos): 
    # Ordena os alunos pela média em ordem decrescente.
    return sorted(alunos.items(), reverse=True, key=lambda item: calcular_media(item[1]))

def recebe_escolha():
    try:
        return int(input("\n"))
    except ValueError:
        print("Por favor, digite um valor válido!")
        pause()
        return None

def menuPrincipal():
    print("\n======= Menu =======")
    print("1 - Cadastrar Aluno")
    print("2 - Opções")
    print("0 - Sair")

def menuOpcoes():
    print("\n======= Opções =======")
    print("1 - Opções por aluno")
    print("2 - Opções da turma")
    print("3 - Ranking da turma")
    print("0 - Voltar para o menu")

def menuAlunos():
    print("\n======= Alunos =======")
    print("1 - Ver alunos cadastrados")
    print("2 - Ver Situação e Média de determinado aluno")
    print("3 - Ver aluno com a melhor média")
    print("4 - Ver aluno com a pior média")
    print("5 - Ver aluno mais consistente")
    print("6 - Ver aluno mais irregular")
    print("0 - Voltar para as opções")

def menuTurma():
    print("\n======= Médias da turma =======")
    print("1 - Ver média das notas (médias) da turma")
    print("2 - Ver média das notas (notas) da turma")
    print("3 - Ver distribuição de notas")
    print("4 - Ver nº de Aprovados, Reprovados e Em Recuperação")
    print("0 - Voltar para as opções")

def menuRanking():
    print("\n======= Ranking =======")
    print("1 - Ranking da turma")
    print("2 - Ver Top 3 alunos")
    print("0 - Voltar para as opções")

def cadastro_aluno(alunos):
    while True:
        nome = input("\nDigite o nome do aluno: ").strip().title()

        if not nome:
            print("Digite algum nome.")
            pause()
            continue

        if nome in alunos:
            print("Aluno já cadastrado.")
        else:
            break
            
    while True:
        try:
            qtde_notas = int(input("\nDigite quantas notas o aluno possui: "))
            if qtde_notas > 0:
                break
            else:
                print("\nDigite um valor maior que 0.")
                pause()
                continue
        except ValueError:
            print("\nPor favor, digite um valor válido!")
            pause()
            continue

    notas_validas = 0
    notas = []

    while notas_validas < qtde_notas:
        try:
            nota = float(input("\nDigite uma nota do usuário: "))
            if verificacao_nota(nota):

                notas.append(nota)
                notas_validas += 1
            else:
                print("\nPor favor, digite um valor válido! (Nota entre 0 e 10)")
                pause()
        except ValueError:
            print("\nPor favor, digite um valor válido!")
            pause()
            continue
            
    alunos[nome] = notas

def opcoes(alunos):
    if alunos:
        while True:
            menuOpcoes()

            escolha = recebe_escolha()

            if escolha is None:
                continue

            if escolha == 1:
                opcao_alunos(alunos)

            elif escolha == 2:
                opcao_turma(alunos)

            elif escolha == 3:
                opcao_ranking(alunos)

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
        menuAlunos()

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
    for aluno in alunos:
        print("-", aluno)
    pause()

def opcao_alunoEspecifico(alunos):
    while True:
        nome_selecionado = input("\nDigite o nome cadastrado que você quer ver situação e média: ").strip().title()
                                    
        if nome_selecionado in alunos:
            situacao, media = situacao_aluno(alunos[nome_selecionado])
            print(f"\n{nome_selecionado} está {situacao} com média de {media:.2f} pontos.")
            pause()
            break
        else:
            print("\nPor favor, digite algum nome válido!")
            pause()

def opcao_melhorAluno(alunos):
    melhor_aluno, media = aluno_melhor(alunos)
    if len(melhor_aluno) == 1:
        print(f"\nO melhor aluno é {melhor_aluno[0]} com a média de {media:.2f} pontos.")
    elif len(melhor_aluno) > 1:
        print(f"\nOs melhores alunos são: {', '.join(melhor_aluno)} com a média de {media:.2f} pontos")
    pause()

def opcao_piorAluno(alunos):
    pior_aluno, media = aluno_pior(alunos)
    if len(pior_aluno) == 1:
        print(f"\nO pior aluno é {pior_aluno[0]} com a média de {media:.2f} pontos.")
    elif len(pior_aluno) > 1:
        print(f"\nOs piores alunos são: {', '.join(pior_aluno)} com a média de {media:.2f} pontos")
    pause()

def opcao_alunoConsistente(alunos):
    consistente, consistencia = aluno_consistente(alunos)
    if len(consistente) == 1:
        print(f"O aluno mais consistente é {consistente[0]} com a diferença de {consistencia} pontos entre as notas.")
    else:
        print(f"Os alunos mais consistentes são: {', '.join(consistente)} com a diferença de {consistencia} pontos entre as notas.")
    pause()

def opcao_alunoIrregular(alunos):
    irregular, consistencia = aluno_irregular(alunos)
    if len(irregular) == 1:
        print(f"O aluno mais irregular é {irregular[0]} com a diferença de {consistencia} pontos entre as notas.")
    else:
        print(f"Os alunos mais irregulares são: {', '.join(irregular)} com a diferença de {consistencia} pontos entre as notas.")
    pause()



def opcao_turma(alunos):
    while True:
        menuTurma()
        
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
    media_da_turma = media_turma_medias(alunos)
    print(f"\nMédia das notas da turma: {media_da_turma:.2f}")
    pause()

def opcao_mediaNotas(alunos):
    media_da_turma = media_turma_notas(alunos)
    print(f"\nMédia das notas da turma: {media_da_turma:.2f}")
    pause()

def opcao_distribuicaoNotas(alunos):
    n10, n8, n6, n4, n2 = qtde_de_notas(alunos)
    print(f"\nNotas tiradas entre 8 e 10: {n10};\nNotas tiradas entre 6 e 8: {n8};\nNotas tiradas entre 4 e 6: {n6};\nNotas tiradas entre 2 e 4: {n4};\nNotas tiradas entre 0 e 2: {n2}")
    pause()

def opcao_aprovados(alunos):
    aprovados, em_recuperacao, reprovados = qtde_aprovacao(alunos)
    print(f"\nAprovados: {aprovados}\nReprovados: {reprovados}\nEm Recuperação: {em_recuperacao}")
    pause()



def opcao_ranking(alunos):
    while True:
        menuRanking()

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
            print("escolha uma das opções.")
            pause()

def opcao_rankingTurma(alunos):
    print(f"\nRanking da turma:")
    for ordem, (aluno, notas) in enumerate(ranking_alunos(alunos), start=1):
        media = calcular_media(notas)
        print(f"{ordem}º - {aluno}, Média: {media:.2f}")

    pause()

def opcao_top3(alunos):
    print("\nTop 3 alunos:")
    for ordem, (aluno, notas) in enumerate(ranking_alunos(alunos), start=1):
        media = calcular_media(notas)
        if ordem <= 3:
            print(f"{ordem}º - {aluno}, Média: {media:.2f}")

    pause()

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

main()