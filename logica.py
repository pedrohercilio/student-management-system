from rich import print
from util import (
    escolher_nota,
    pause,
    ler_float,
    ler_int
)

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

def ranking_alunos(alunos):
    # Ordena os alunos pela média em ordem decrescente.
    return sorted(alunos.items(), reverse=True, key=lambda item: calcular_media(item[1]))

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

def editar_nome(alunos, nome_selecionado):
    while True:
        novo_nome = input(f"\nQual o nome que você quer colocar no lugar de {nome_selecionado}? ").strip().title()
        if novo_nome and novo_nome not in alunos:
           alunos[novo_nome] = alunos.pop(nome_selecionado)
           break

        if novo_nome == nome_selecionado:
            print("\nO novo nome é igual ao nome atual. Escolha outro nome.")
            pause()
        else:
            print("\nO nome escolhido já está entre os atuais alunos ou está vazio, por favor, digite outro nome.")
            pause()
    print("Nome alterado com êxito!")

def editar_quantidadeNotas(quantidade_notas, notas, nome_selecionado):
    while True:
        nova_quantidade = ler_int(f"\nQual a nova quantidade de notas que {nome_selecionado} terá? ")

        if nova_quantidade <= 0:
            print("\nPor favor, digite uma quantidade válida (maior que zero).")
            pause()
            continue
        

        if nova_quantidade > quantidade_notas:
            novaquantidade_maior(nova_quantidade, quantidade_notas, notas)
            return


        elif nova_quantidade == quantidade_notas:
            print("\nA nova quantidade de notas é a mesma da já existente, tente novamente.")
            pause()
            continue

        novaquantidade_menor(quantidade_notas, nova_quantidade, notas)
        return

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

        if not numero_selecionado:
            print("\nSelecione alguma nota.")
            pause()
            continue
        
        if numero_selecionado is not None and 1 <= numero_selecionado <= len(notas):
            notas.pop(numero_selecionado - 1)
            print("\nNota removida com êxito!")
            break
        else:
            print("\nPor favor, selecione uma nota válida.")

def diferenca_maior(notas, diferenca, quantidade_notas):
    print(f"\nA nova quantidade escolhida é menor que a quantidade de notas atual, será necessário retirar {diferenca} notas.")
    pause()

    while True:

        notas_para_remover = ler_notas_remover(notas, diferenca)

        itens_para_corrigir, indices_validos = validar_notas(notas, notas_para_remover)
        
        corrigir_notas(itens_para_corrigir, notas, quantidade_notas, indices_validos)

        if remover_notas(diferenca, indices_validos, notas):
            break        

def ler_notas_remover(notas, diferenca):
    print("\nNotas atuais:")
    for i, nota in enumerate(notas):
        print(f"{i + 1} - {nota}")
    print("\n______________________________")

    while True:
        notas_para_remover = []
        print(f"\nDigite as {diferenca} notas a remover:\n")
        while len(notas_para_remover) < diferenca:
            nota_recebida = input("> ")
            notas_separadas = nota_recebida.split()
            for nota in notas_separadas:
                notas_para_remover.append(nota)
        if len(notas_para_remover) != diferenca:
            print(f"\nDigite exatamente {diferenca} notas.")
            pause()
            continue
        
        if len(notas_para_remover) == diferenca:
            return notas_para_remover
        else:
            print("\nVocê digitou mais notas do que o necessário, por favor, digite-as novamente.")
            pause()

def validar_notas(notas, notas_para_remover):
    # Listas para separar as entradas válidas das não válidas (joio do trigo)
    indices_validos = []
    itens_para_corrigir = [] # Armazena tuplas: (índice_na_entrada, valor_digitado)
    
    # 2 - validação inicial
    for i, valor in enumerate(notas_para_remover):
        valor_limpo = valor.strip().title()
        numero_selecionado = escolher_nota(valor_limpo, len(notas_para_remover))

        
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
            itens_para_corrigir.append({'Posicao': i, 'Valor': valor, 'Motivo': motivo})

    return itens_para_corrigir, indices_validos
        
def corrigir_notas(itens_para_corrigir, notas, quantidade_notas, indices_validos):
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

def remover_notas(diferenca, indices_validos, notas):
    if len(indices_validos) == diferenca:
        indices_validos.sort(reverse=True)
        for indice in indices_validos:
            notas.pop(indice - 1)
        print(f"\n{diferenca} notas removidas com êxito!")
        return True

def editar_nota(quantidade_notas, notas):
    while True:
        print('\n')
        for i in range (quantidade_notas):
            print(f"Nota {i + 1}: {notas[i]}")
        nota_selecionada = input(f"Qual das {quantidade_notas} notas atuais você quer editar? ")

        numero_selecionado = escolher_nota(nota_selecionada, quantidade_notas)

        if not numero_selecionado:
            print("\nSelecione alguma nota.")
            pause()
            continue
        
        if 1 <= numero_selecionado <= quantidade_notas:

            print(f"\nA nota {numero_selecionado} é {notas[numero_selecionado - 1]}.")

            while True:
                nova_nota = ler_float("\nQual será o valor da nova nota? ")
                if verificacao_nota(nova_nota):
                    break
                else:
                    print("\nPor favor, digite uma nota válida! (Nota entre 0 e 10).")
                    pause()

            
            notas[numero_selecionado - 1] = nova_nota
            print("\nNota atualizada com sucesso!")
            break

        else:
            print("\nPor favor, selecione uma nota válida.")
            pause()
