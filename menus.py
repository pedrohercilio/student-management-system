from rich import print

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
