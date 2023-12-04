valor = input('Digite algo:')

print('Seu tipo é: {} ; É um caracter? {} É um número? {}'.format(type(valor), valor.isalpha(), valor.isalnum()))