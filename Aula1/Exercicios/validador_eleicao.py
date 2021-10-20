nome = input('Qual o seu nome? R: ')
idade = int(input('Qual a sua idade? R: '))

if idade >= 18:
    msg = 'E você deverá votar nas eleições!'
elif idade > 16 and idade < 18:
    msg = 'E você tem a opção de votar nas eleições!'
else:
    msg = 'E você não poderá votar nas eleições ainda!'

print('\nInformações técnicas apresentadas:\n')
print('O seu nome é '+nome+', ele possui exatos '+str(len(nome))+' caracteres.\n')
print('Você informou a idade '+str(idade)+' e ela é do tipo '+str(type(idade))+'\n')
print(msg+'\n')
input('Pressione "ENTER" para encerrar o programa')