peso = float(input('Qual o seu peso?\nR: '))
altura = float(input('Qual a sua altura?\nR: '))

multi = altura * altura

imc = peso / multi

print(f'\nSeu IMC é de {imc:.2f}')

if imc < 18.5:
    print('\nE você está abaixo do peso!')
elif imc > 24.9:
    print('\nE você está com sobrepeso!')
else:
    print('\nE você está no peso ideal!')

input('\nPressione "Enter" para fechar!')
