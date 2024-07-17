# Crie um pequeno sistema modularizado que permita cadastrar pessoas
# pelo seu nome e idade em um arquivo de texto simples.
# O sistema só vai ter 2 opções: cadastrar uma nova pessoa e listar
# todas as pessoas cadastradas.
from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2)
