from math import hypot,trunc

cato = int(input('Digite o valor do cateto oposto: '))
cata = int(input('Digite o valor do cateto adjacente: '))
hipo = hypot(cato, cata)
print('O valor da hipotenusa é iguaal a {}'.format(trunc(hipo)))
