from rich import print
from util import (
    pause,
    ler_float,
    ler_int
)
from logica import verificacao_nota
import json



def ler_json():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
        return alunos

def cadastrar_matricula(alunos, novo_aluno):
    # Calcula o próximo número de referência (chave do JSON) de forma robusta
    try:
        maior = max(int(k) for k in alunos.keys())
    except ValueError:
        maior = 0
    num_matricula = maior + 1
    # Valor de matrícula usado dentro do registro (ex: "01", "02")
    novo_aluno["matricula"] = str(num_matricula).zfill(2)
    return num_matricula
        
def cadastrar_nome(alunos, novo_aluno):
    while True:

        validacao = False
        nome = input("\nDigite o nome do aluno: ").strip().title()
        sobrenome = input("\nDigite o sobrenome do aluno: ").strip().title()
        nome_completo = nome + " " + sobrenome

        if not nome or not sobrenome:
            print("\nDigite algum nome.")
            pause()
            continue

        # Verifica existência de aluno com mesmo nome
        for i in range(1, len(alunos) + 1):
            key = str(i)
            if key in alunos and nome_completo == alunos[key].get("nome"):
                print("\nAluno já cadastrado.")
                pause()
                break
        else:
            # Não encontrou, valida
            novo_aluno["nome"] = nome_completo
            break 

def cadastrar_idade(novo_aluno):
    idade = ler_int("\nDigite a idade do aluno: ")
    novo_aluno["idade"] = idade

def cadastrar_notas():
    # Placeholder por enquanto
    pass


def salvar_aluno_em_json(alunos, novo_aluno, num_referencia):
    # Adiciona o novo aluno ao dicionário e grava em dados.json
    alunos[str(num_referencia)] = novo_aluno
    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, ensure_ascii=False, indent=4)

def cadastro_aluno():

    alunos = ler_json()

    novo_aluno = {"matricula": "",
                  "nome": "",
                  "idade": 0,
                  "notas": []
                 }

    num_referencia = cadastrar_matricula(alunos, novo_aluno)

    cadastrar_nome(alunos, novo_aluno)

    cadastrar_idade(novo_aluno)

    print("\nmatricula, nome e idade cadastrados com sucesso!\n")
    print(novo_aluno)

    # Salva o novo aluno no arquivo dados.json com a próxima chave numérica
    salvar_aluno_em_json(alunos, novo_aluno, num_referencia)
    print(f"\nAluno salvo em dados.json com referência {num_referencia}.")

cadastro_aluno()