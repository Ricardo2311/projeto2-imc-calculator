peso = int(input('d'))
altura = float(input('d'))

imc = peso/(altura**2)
if imc < 17:
    print('Muito abaixo do peso')
elif imc <= 18.5:
    print('Abaixo do peso')
elif imc <= 24.9:
    print('Peso normal')
elif imc <= 29.9:
    print('Acima do peso')
elif imc < 34.9:
    print('Obesidade I')
elif imc < 39.9:
    print('Obesidade II(severa)')
else:
    print('Obesidade III(mórbida)')
