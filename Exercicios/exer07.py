n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('A soma é {0}, o produto é {1} e a divisão é {:.3f}'.format(n1+n2, n1*n2, n1/n2), end='')
#:.3f aqui é formatação de três pontos flutuantes 
# Aqui não dá o pulo end=''
# Para dar quebra de linha é \n