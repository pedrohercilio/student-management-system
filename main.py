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

    return nome_selecionado

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
    print("4 - Gerenciamento dos alunos")
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

def menuGerenciarAlunos():
    print("\n===== Gerenciamento de Alunos =====")
    print("1 - Ver informações dos alunos")
    print("2 - Editar informações dos alunos")
    print("3 - Excluir determinado aluno")
    print("0 - Voltar para o menu")

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
    for aluno in sorted(alunos):
        print("-", aluno)
    pause()

def opcao_alunoEspecifico(alunos):
    print("\nSituação e média de determinado aluno:")

    while True:
        nome_selecionado = escolher_aluno(alunos)

        if nome_selecionado is not None and nome_selecionado in alunos:
            situacao, media = situacao_aluno(alunos[nome_selecionado])
            print(f"\n{nome_selecionado} está {situacao} com média de {media:.2f} pontos.")
            pause()
            break

        else:
            print("\nPor favor, selecione algum aluno válido!")
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
        print(f"O aluno mais consistente é {consistente[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais consistentes são: {', '.join(consistente)} com a diferença de {consistencia:.2f} pontos entre as notas.")
    pause()

def opcao_alunoIrregular(alunos):
    irregular, consistencia = aluno_irregular(alunos)
    if len(irregular) == 1:
        print(f"O aluno mais irregular é {irregular[0]} com a diferença de {consistencia:.2f} pontos entre as notas.")
    else:
        print(f"Os alunos mais irregulares são: {', '.join(irregular)} com a diferença de {consistencia:.2f} pontos entre as notas.")
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
            print("Escolha uma das opções.")
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

def opcao_gerenciarAlunos(alunos):
    while True:
        menuGerenciarAlunos()

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
        media = calcular_media(notas)

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
                media = calcular_media(notas)

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
                    editar_nome(alunos, nome_selecionado)
                    break

                elif escolha == 2:
                    editar_quantidadeNotas(qtde_notas, notas, nome_selecionado)
                    break

                elif escolha == 3:
                    editar_nota(qtde_notas, notas)
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



def editar_nome(alunos, nome_selecionado):
    while True:
        novo_nome = input(f"\nQual o nome que você quer colocar no lugar de {nome_selecionado}? ").strip().title()
        if novo_nome not in alunos:
           alunos[novo_nome] = alunos.pop(nome_selecionado)
           break
        else:
            print("\nO nome escolhido já está entre os atuais alunos, por favor, digite outro nome.")
            pause()
    print("Nome alterado com êxito!")

def editar_quantidadeNotas(quantidade_notas, notas, nome_selecionado):

    nova_quantidade = ler_int(f"\nQual a nova quantidade de notas que {nome_selecionado} terá? ")


    if nova_quantidade > quantidade_notas:
        novaquantidade_maior(nova_quantidade, quantidade_notas, notas)
        return


    elif nova_quantidade == quantidade_notas:
        print("\nA nova quantidade de notas é a mesma da já existente, tente novamente.")
        pause()
        return

    novaquantidade_menor(quantidade_notas, nova_quantidade, notas)


def novaquantidade_maior(nova_quantidade, quantidade_notas, notas):
    for i in range (1, nova_quantidade - quantidade_notas + 1):
        nota_valida = 0
        while nota_valida == 0:
            nova_nota = ler_float(f"\nDigite a {i + quantidade_notas}ª (nova) nota: ")
            if verificacao_nota(nova_nota):

                notas.append(nova_nota)
                nota_valida = 1
            else:
                print("\nPor favor, digite uma nota válida! (Nota entre 0 e 10)")
                pause()

    print("\nNota(s) adicionada(s) com êxito!")

def novaquantidade_menor(quantidade_notas, nova_quantidade, notas):
    diferenca = quantidade_notas - nova_quantidade

    if diferenca == 1:
        diferenca_igual(quantidade_notas, notas)

    elif diferenca > 1:
        diferenca_maior(notas, diferenca, quantidade_notas)

def diferenca_igual(quantidade_notas, notas):
    print(f"\nA nova quantidade escolhida é menor que a quantidade de notas atual, será necessário retirar 1 nota.")
    while True:
        for i in range (quantidade_notas):
            print(f"Nota {i + 1}: {notas[i]}")
        nota_selecionada = input(f"\nQual das {quantidade_notas} notas atuais você quer retirar? ")

        numero_selecionado = escolher_nota(nota_selecionada, quantidade_notas)

        if numero_selecionado is not None and 1 <= numero_selecionado <= len(notas):
            notas.remove(notas[numero_selecionado - 1])
            print("\nNota removida com êxito!")
            break
        else:
            print("\nPor favor, selecione uma nota válida.")

def diferenca_maior(notas, diferenca, quantidade_notas):
    print(f"\nA nova quantidade escolhida é menor que a quantidade de notas atual, será necessário retirar {diferenca} notas.")
    pause()

    while True:

        print("\nNotas atuais:")
        for i, nota in enumerate(notas):
            print(f"{i + 1} - {nota}")
        pause()

        notas_para_remover = []
        print(f"\nDigite as {diferenca} notas a remover:\n")
        while len(notas_para_remover) < diferenca:
            nota_recebida = input("> ")
            notas_separadas = nota_recebida.split()
            for nota in notas_separadas:
                notas_para_remover.append(nota)
        print(notas_para_remover)
        
        # Listas para separar as entradas válidas das não válidas (joio do trigo)
        indices_validos = []
        itens_para_corrigir = [] # Armazena tuplas: (índice_na_entrada, valor_digitado)
        
        # 2 - validação inicial
        for i, p in enumerate(notas_para_remover):
            parte_limpo = p.strip().title()
            numero_selecionado = escolher_nota(parte_limpo, len(notas_para_remover))

            
            valido = True
            
            if numero_selecionado is None:
                valido = False
                motivo = "Valor inválido."

            elif not (1 <= numero_selecionado <= len(notas)):
                valido = False
                motivo = f"Fora do intervalo (1 - {len(notas)})."

            elif numero_selecionado in indices_validos:
                valido = False
                motivo = "Repetido (você já selecionou esta nota)."

            
            if valido:
                indices_validos.append(numero_selecionado)
            else:
                itens_para_corrigir.append({'Posicao': i, 'Valor': p, 'Motivo': motivo})


        if itens_para_corrigir:
            print(f"\nSerá necessário corrigir {len(itens_para_corrigir)} erros/valores enviados:")
            for valor, item in enumerate(itens_para_corrigir):
                print(f"{valor + 1} - '{item['Valor']}': {item['Motivo']}")
            
            print("\n--- Correção dos itens inválidos ---")
            
            for item in itens_para_corrigir:
                while True:
                    novo_valor = input(f"\nSubstitua '{item['Valor']}' por causa de {item['Motivo']}: ").strip().title()
                    novo_num = None
                    
                    try:
                        novo_num = int(novo_valor)
                    except ValueError:
                        if novo_valor.startswith("Nota"):
                            try: 
                                novo_num = int(novo_valor.split()[1])
                            except: 
                                pass
                        if novo_num is None:
                            for i in range(len(notas)):
                                if novo_valor == f"Nota {i + 1}":
                                    novo_num = i + 1
                                    break
                    
                    if novo_num is None:
                        print("Valor não reconhecido, utilize número ou 'Nota X'.")
                        pause()
                        continue

                    if not (1 <= novo_num <= quantidade_notas):
                        print(f"Valor fora da quantidade estabelecida (1 - {quantidade_notas})")
                        pause()
                        continue

                    if novo_num in indices_validos:
                        print("Nota já selecionada, escolhida ou corrigida.")
                        pause()
                        continue
                    
                    indices_validos.append(novo_num)
                    print("Novo valor aceito!")
                    break

        if len(indices_validos) == diferenca:
            indices_validos.sort(reverse=True)
            for indice in indices_validos:
                notas.pop(indice - 1)
            print(f"\n{diferenca} notas removidas com êxito!")
            break


def editar_nota(quantidade_notas, notas):
    while True:
        print('\n')
        for i in range (quantidade_notas):
            print(f"Nota {i + 1}: {notas[i]}")
        nota_selecionada = input(f"Qual das {quantidade_notas} notas atuais você quer editar? ")

        numero_selecionado = escolher_nota(nota_selecionada, quantidade_notas)

        if 1 <= numero_selecionado <= quantidade_notas:

            print(f"\nA nota {numero_selecionado} é {notas[numero_selecionado - 1]}.")

            while True:
                nova_nota = ler_float("\nQual será o valor da nova nota? ")
                if verificacao_nota(nova_nota):
                    break

            if numero_selecionado is not None and 1 <= numero_selecionado <= len(notas):
                notas[numero_selecionado - 1] = nova_nota
                print("\nNota atualizada com sucesso!")
                break

        else:
            print("\nPor favor, selecione uma nota válida.")
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

def main():
    # Alunos para exemplo de execução do código
    alunos = {"Pedro": [8.0, 9.0],
              "Maria": [9.0, 5.4],
              "Joao": [7.8, 8.1],
              "José": [6.4, 4.9],
              "Ana": [7.8, 5.9]}

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