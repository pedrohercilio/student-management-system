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
        registros = json.load(arquivo)

    if not isinstance(registros, dict):
        raise ValueError("dados.json deve conter um objeto JSON de alunos.")

    alunos = {}
    for referencia, aluno in registros.items():
        if not referencia.isdigit():
            raise ValueError(f"A referência do aluno {referencia} deve ser numérica.")
        if not isinstance(aluno, dict):
            raise ValueError(f"O registro do aluno {referencia} deve ser um objeto.")

        campos_obrigatorios = ("matricula", "nome", "idade", "notas")
        if any(campo not in aluno for campo in campos_obrigatorios):
            raise ValueError(f"O registro do aluno {referencia} não contém todos os campos obrigatórios.")
        if not isinstance(aluno["nome"], str) or not isinstance(aluno["notas"], list):
            raise ValueError(f"O registro do aluno {referencia} possui campos inválidos.")
        if aluno["nome"] in alunos:
            raise ValueError(f"Há mais de um aluno com o nome {aluno['nome']}.")

        registro = aluno.copy()
        registro["_referencia"] = str(referencia)
        alunos[registro["nome"]] = registro

    return alunos


def salvar_json(alunos):
    registros = {}
    for nome, aluno in alunos.items():
        referencia = str(aluno["_referencia"])
        registro = {
            campo: valor
            for campo, valor in aluno.items()
            if campo != "_referencia"
        }
        registro["nome"] = nome
        registros[referencia] = registro

    with open("dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, ensure_ascii=False, indent=4)

def cadastrar_matricula(alunos, novo_aluno):
    maior = max(
        (int(aluno["_referencia"]) for aluno in alunos.values()),
        default=0
    )
    referencia = str(maior + 1)
    novo_aluno["_referencia"] = referencia
    novo_aluno["matricula"] = referencia.zfill(2)
    return referencia
        
def cadastrar_nome(alunos, novo_aluno):
    while True:

        nome = input("\nDigite o nome do aluno: ").strip().title()
        sobrenome = input("\nDigite o sobrenome do aluno: ").strip().title()
        nome_completo = nome + " " + sobrenome

        if not nome or not sobrenome:
            print("\nDigite algum nome.")
            pause()
            continue

        if nome_completo not in alunos:
            novo_aluno["nome"] = nome_completo
            break
        print("\nAluno já cadastrado.")
        pause()

def cadastrar_idade(novo_aluno):
    idade = ler_int("\nDigite a idade do aluno: ")
    novo_aluno["idade"] = idade

def cadastrar_notas(novo_aluno):
    while True:
        quantidade_notas = ler_int("\nDigite quantas notas o aluno possui: ")
        if quantidade_notas > 0:
            break
        print("\nDigite um valor maior que 0.")
        pause()

    while len(novo_aluno["notas"]) < quantidade_notas:
        nota = ler_float("\nDigite uma nota do aluno: ")
        if verificacao_nota(nota):
            novo_aluno["notas"].append(nota)
        else:
            print("\nDigite uma nota válida entre 0 e 10.")
            pause()


def cadastro_aluno(alunos):
    novo_aluno = {"matricula": "",
                  "nome": "",
                  "idade": 0,
                  "notas": []
                 }

    cadastrar_matricula(alunos, novo_aluno)

    cadastrar_nome(alunos, novo_aluno)

    cadastrar_idade(novo_aluno)

    cadastrar_notas(novo_aluno)

    print("\nMatrícula, nome, idade e notas cadastrados com sucesso!\n")
    alunos[novo_aluno["nome"]] = novo_aluno