from math import cos, sin, tan

ang = int(input('Digite um angulo: '))
coss = cos(ang)
seno = sin(ang)
tg = tan(ang)
print('O angulo {} tem como seno {:.2f} , como cosseno {:.2f} e como tangente {:.2f}'.format(ang, seno, coss, tg))
