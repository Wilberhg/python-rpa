frase = input("Por favor, insira uma frase: ").strip()
primeira_palavra = frase[:frase.find(' ')]
ultima_palavra = frase[frase.rfind(' '):]
frase_sem_palavras = frase[frase.find(' '):frase.rfind(' ')]
frase_maiuscula = frase.upper()
frase_minuscula = frase.lower()
print(f'\nA primeira palavra da frase é: "{primeira_palavra.strip()}"')
print(f'\nA última palavra da frase é: "{ultima_palavra.strip()}"')
print(f'\nA frase sem a primeira e última palavra é: "{frase_sem_palavras.strip()}"')
print(f'\nA frase com tudo maiúsculo é: "{frase_maiuscula}"')
print(f'\nA frase com tudo minúsculo é: "{frase_minuscula}"\n')
input('Pressione "Enter" para fechar o programa')
