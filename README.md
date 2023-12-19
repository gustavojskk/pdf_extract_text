Extrair Texto e Gerar Questões de PDFs em Python

Este projeto extrai o texto de um arquivo PDF e gera perguntas baseadas no conteúdo principal. Ele usa as seguintes bibliotecas:

PyMuPDF (fitz): Para extrair o texto dos arquivos PDF.
NLTK: Para tokenização de sentenças e outras tarefas de processamento de linguagem natural.
Funcionalidades:

Extrair o texto de um arquivo PDF.
Dividir o texto em tópicos baseados em parágrafos.
Gerar perguntas para cada tópico, usando as primeiras frases de cada sentença.
Salvar as perguntas em um arquivo JSON.
Demonstração:

O código principal (main.py) demonstra o uso das funções para extrair texto e gerar perguntas a partir do arquivo "khomp.pdf". As perguntas serão salvas em "saida.json".

Pré-requisitos:

Python 3.x
Bibliotecas: PyMuPDF (fitz), NLTK
Instalação:

Instale o Python e as bibliotecas necessárias:
pip install fitz nltk
Baixe os modelos do NLTK:
python -m nltk download punkt
Uso:

Execute o código principal:
python pdf.py
Saída:

O arquivo "saida.json" conterá uma lista de dicionários, cada um representando um tópico e suas respectivas perguntas.

Exemplo de saída:

[
  {
    "topic": "O que é a Khomp?",
    "questions": [
      "O que é a Khomp?",
      "Quais são as principais funcionalidades da Khomp?"
    ]
  },
  {
    "topic": "Instalação da Khomp",
    "questions": [
      "Como instalar a Khomp?",
      "Quais são os requisitos de sistema para a Khomp?"
    ]
  },
  ...
]

