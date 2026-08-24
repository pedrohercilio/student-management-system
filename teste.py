from rich import print
from util import (
    pause,
    ler_float,
    ler_int
)
from logica import verificacao_nota
from email_validator import validate_email, EmailNotValidError
import phonenumbers
from phonenumbers import NumberParseException
import json

def ler_json():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
        return alunos


def verificar_email_completo(email):
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False

    
def verificar_celular_completo(telefone_digitado):
    try:
        # Ele aceita formatos como: "51999999999", "(51) 99999-1111", "51 999991111"
        numero_objeto = phonenumbers.parse(telefone_digitado, "BR")
        
        # 1. Verifica se o número é estruturalmente válido (tamanho, formato e DDD existente)
        if not phonenumbers.is_valid_number(numero_objeto):
            return False, None

        # Retorna True e o número formatado no padrão internacional E.164 (+5551999999999)
        # Esse padrão limpo é o ideal para salvar no banco de dados
        numero_limpo = phonenumbers.format_number(numero_objeto, phonenumbers.PhoneNumberFormat.E164)
        return True, numero_limpo
        
    except NumberParseException:
        # Se o usuário digitar letras ou algo que quebre o interpretador
        return False, None





def cadastro_aluno():

    alunos = ler_json()

    novo_aluno = {"nome": "",
                  "idade": 0,
                  "e-mail": "",
                  "celular": "",
                  "CPF": "",
                  "ensino":{
                      "escolaridade": "",
                      "curso": "",
                      "condição": "",
                      "semestre":{
                        
                            "Engenharia de Software: Fundamentos":{
                                "dia": "Segunda-Feira",
                                "notas_GA": [],
                                "notas_GB": [],
                                "notas_GC": []
                            },
                            "Sistemas Digitais":{
                                "dia": "Terça-Feira",
                                "notas_GA": [],
                                "notas_GB": [],
                                "notas_GC": []
                            },
                            "Algoritmos e Programação: Orientação a Objetos":{
                                "dia": "Quarta-Feira",
                                "notas_GA": [],
                                "notas_GB": [],
                                "notas_GC": []
                            },
                            "Cálculo Diferencial":{
                                "dia": "Quinta-Feira",
                                "notas_GA": [],
                                "notas_GB": [],
                                "notas_GC": []
                            },
                            "Álgebra Linear e Geometria Analítica":{
                                "dia": "Sexta-Feira",
                                "notas_GA": [],
                                "notas_GB": [],
                                "notas_GC": [] 
                            }
                        }
                      }
                 }
    # cadastro do nome
    while True:

        validacao = False
        nome = input("\nDigite o nome do aluno: ").strip().title()
        sobrenome = input("\nDigite o sobrenome do aluno: ").strip().title()
        nome_completo = nome + " " + sobrenome

        if not nome or not sobrenome:
            print("Digite algum nome.")
            pause()
            continue

        for i in range(1, len(alunos)):
            if nome_completo in alunos[str(i)]["nome"]:
                print("\nAluno já cadastrado.")
                pause()
                continue
            else:
                validacao = True

        if validacao:
            novo_aluno["nome"] = nome_completo
            break    


    # cadastro da idade
    idade = ler_int("\nDigite a idade do aluno: ")
    novo_aluno["idade"] = idade


    # cadastro do email
    while True:
        email = input("\nDigite o email do aluno: ").strip().lower()
        email2 = input("\nConfirme o email do aluno: ").strip().lower()
        if email == email2:
            if verificar_email_completo(email):
                novo_aluno["e-mail"] = email
                break
            else:
                print("\nPor favlor, digite um email válido.")
        else:
            print("\nOs emails digitados não correspondem, por favor digite-os novamente.")


    # cadastro do celular
    while True:
        pass




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

print(ler_json())
cadastro_aluno()