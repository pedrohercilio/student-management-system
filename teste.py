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
from validate_docbr import CPF



def ler_json():
    with open("dados.json", "r", encoding="utf-8") as arquivo:
        alunos = json.load(arquivo)
        return alunos


def verificar_email(email):
    try:
        validate_email(email, check_deliverability=True)
        return True
    except EmailNotValidError:
        return False

    
def verificar_celular(celular):
    try:
        numero_formatado = phonenumbers.parse(celular, "BR")
        
        if not phonenumbers.is_valid_number(numero_formatado):
            return False, None

        # Formato do número> E.164 (+5551999999999)
        numero_limpo = phonenumbers.format_number(numero_formatado, phonenumbers.PhoneNumberFormat.E164)
        return True, numero_limpo
        
    except NumberParseException:
        return False, None

def celular_paraLeitura(celular):
    # Formato do número> INTERNATIONAL (+55 (51) 91111-2222)
    numero_objeto = phonenumbers.parse(celular, "BR")
    return phonenumbers.format_number(numero_objeto, phonenumbers.PhoneNumberFormat.INTERNATIONAL)

def verificar_cpf(cpf):
    cpf_limpo = "".join(char for char in cpf if char.isdigit())
    validador = CPF()

    if validador.validate(cpf_limpo):
        return True, cpf_limpo
    else:
        return False, None

def cpf_paraLeitura(cpf):
    validador = CPF()
    return validador.mask(cpf)




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
            if verificar_email(email):
                novo_aluno["e-mail"] = email
                break
            else:
                print("\nPor favlor, digite um email válido.")
        else:
            print("\nOs emails digitados não correspondem, por favor digite-os novamente.")


    # cadastro do celular
    while True:
        celular = input("\nDigite o número de celular do aluno: ")
        if verificar_celular(celular):
            novo_aluno["celular"] = celular
            break
        else:
            print("\nPor favor, digite um número de celular válido")


    # cadastro do CPF
    while True:
        cpf = input("\nDigite o CPF do aluno: ")
        if verificar_cpf(cpf):
            novo_aluno["CPF"] = cpf
            break
        else:
            print("\nPor favor, digite um CPF válido.")

    # cadastro da escolaridade
