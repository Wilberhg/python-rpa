valor = int(input('Por favor insira um número para ver a tabuada dele: '))
print()
for i in range(1, 11):
    print(f'{i} x {valor} = {i*valor}')

input('\nPressione "Enter" para sair')
