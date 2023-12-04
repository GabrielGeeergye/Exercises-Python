import math

cat1 = int(input('Digite o primeiro adjacente cateto: '))
cat3 = int(input('Digite o segundo oposto cateto: '))

hip = math.sqrt(cat1 *cat1  + cat3*cat3)

print('A hipotenusa é: {}'.format(math.ceil(hip)))