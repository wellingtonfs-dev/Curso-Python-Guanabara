# Faça um programa que tenha uma função notas() que pode receber várias notas
# de alunos e vai retornar um dicionário com os seguintes informações:
# - Quantidade de notas
# - A maior nota
# - A menor nota
# - A média da turma
# - A situação(opcional)
# Adicione também as docstrings.
import sys


def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos.
    :param sit: Valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    relatorio = dict()
    relatorio['total'] = len(n)
    relatorio['maior'] = max(n)
    relatorio['menor'] = min(n)
    relatorio['media'] = sum(n)/len(n)
    if sit:
        if relatorio['media'] >= 7:
            relatorio['situação'] = 'Ótimo'
        elif relatorio['media'] >= 5:
            relatorio['situação'] = 'Razoável'
        else:
            relatorio['situação'] = 'Ruim'
    return relatorio


resp = notas(5.5, 2.5, 8.5)
print(resp)
