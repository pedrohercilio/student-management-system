from main import pause
from main import escolher_nota

def ler_notas_remover(notas, diferenca):
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
    return notas_para_remover

def validar_notas(notas, notas_para_remover):
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

def diferenca_maior(notas, diferenca, quantidade_notas):
    print(f"\nA nova quantidade escolhida é menor que a quantidade de notas atual, será necessário retirar {diferenca} notas.")
    pause()

    while True:

        notas_para_remover = ler_notas_remover(notas, diferenca)

        itens_para_corrigir, indices_validos = validar_notas(notas, notas_para_remover)
        
        corrigir_notas(itens_para_corrigir, notas, quantidade_notas, indices_validos)

        if remover_notas(diferenca, indices_validos, notas):
            break        