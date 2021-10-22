import random
lista_de_alunos = []
while len(lista_de_alunos) < 5:
    tamanho_lista = len(lista_de_alunos)
    nome = input(f'Por favor insira o nome do aluno de número {tamanho_lista+1}: ')
    lista_de_alunos.append(nome)
print(f'\nA ordenação era: {lista_de_alunos}')
random.shuffle(lista_de_alunos)
print(f'\nA ordenação ficou assim: {lista_de_alunos}\n')
input('Pressione "Enter" para encerrar')
