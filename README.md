# 🎓 Sistema de Gerenciamento de Alunos

Sistema de gerenciamento acadêmico desenvolvido em Python, executado através do terminal.

O projeto permite cadastrar e gerenciar alunos e notas, realizar análises de desempenho da turma e manter todas as informações salvas em arquivo JSON entre uma execução e outra.

---

## 📌 Funcionalidades

**Alunos**
- Cadastro de alunos com matrícula gerada automaticamente
- Edição de nome, idade, quantidade de notas e notas individuais
- Exclusão de alunos com confirmação
- Consulta de todas as informações cadastradas
- Seleção do aluno pelo número da lista ou pelo nome

**Notas e desempenho**
- Cálculo de média e situação acadêmica (Aprovado, em Recuperação ou Reprovado)
- Aluno com a melhor e a pior média (com tratamento de empates)
- Aluno mais consistente e mais irregular (menor e maior diferença entre as notas)

**Turma**
- Média da turma (média das médias e média de todas as notas)
- Distribuição de notas por faixa
- Quantidade de aprovados, reprovados e em recuperação
- Ranking completo e Top 3 alunos

**Geral**
- Persistência dos dados em arquivo JSON
- Validação das entradas do usuário e do conteúdo do arquivo de dados
- Interface baseada em menus interativos
- Tratamento de erros utilizando exceções

---

## 📏 Regras de negócio

| Situação | Critério |
|----------|----------|
| Aprovado | média ≥ 7 |
| Em Recuperação | 5 ≤ média < 7 |
| Reprovado | média < 5 |

- As notas devem estar entre **0 e 10**.
- Cada aluno deve ter ao menos **uma nota** e idade maior que **0**.
- Não é possível cadastrar dois alunos com o mesmo nome.

---

## 🛠 Tecnologias

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) (saída formatada no terminal)
- JSON (armazenamento e persistência de dados)
- Git / GitHub

---

## 🗂 Estrutura do projeto

```
student-management-system/
├── main.py        # Ponto de entrada e menu principal
├── menus.py       # Textos dos menus
├── opcoes.py      # Fluxo das opções (alunos, turma, ranking e gerenciamento)
├── cadastro.py    # Cadastro de novos alunos
├── logica.py      # Cálculos, edição de dados e leitura/gravação do JSON
├── util.py        # Funções auxiliares de entrada e seleção
└── dados.json     # Arquivo de dados (criado automaticamente se não existir)
```

---

## 💾 Persistência dos dados

Os dados são carregados do arquivo `dados.json` ao iniciar o programa e **gravados somente ao sair pelo menu principal (opção `0 - Sair`)**. Encerrar o programa de outra forma (fechar o terminal ou `Ctrl+C`) descarta as alterações feitas na sessão.

- Se o arquivo não existir ou estiver vazio, ele é criado automaticamente.
- Se o arquivo estiver corrompido ou com estrutura inválida, o programa informa o problema e permite tentar carregar novamente após a correção.

Formato do arquivo:

```json
{
    "1": {
        "matricula": "01",
        "nome": "Maria Silva",
        "idade": 18,
        "notas": [8.5, 7.0, 9.0]
    }
}
```

A chave de cada registro é um número de referência e a matrícula é gerada a partir dele.

---

## 📚 Conceitos aplicados

- Programação estruturada
- Funções e modularização
- Listas e dicionários
- Validação e tratamento de exceções
- Estruturas condicionais e de repetição
- Leitura e escrita de arquivos JSON
- Validação da estrutura de dados externos
- Uso de bibliotecas de terceiros
- Versionamento com Git

---

## 🎯 Objetivo

Projeto desenvolvido para praticar e consolidar conhecimentos em Python e lógica de programação, evoluindo gradualmente conforme novos conceitos eram aprendidos.

---

## ▶️ Como executar

Clone o repositório:

```bash
git clone https://github.com/pedrohercilio/student-management-system.git
```

Entre na pasta:

```bash
cd student-management-system
```

Instale a dependência:

```bash
python -m pip install rich
```

Execute (a partir da pasta do projeto):

```bash
python main.py
```

---

## 👨‍💻 Autor

**Pedro Hercílio Montezano Alves**

GitHub: [pedrohercilio](https://github.com/pedrohercilio)