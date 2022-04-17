name = input('Digite o seu nome: ')
weight = int(input('Digite o seu peso: '))
height = float(input('Digite a sua altura: '))

bmi = weight / (height * height)
bmi = round(bmi, 2)

if bmi < 18.5:
    classification = 'Abaixo do Peso!'

elif bmi >= 18.5 and bmi <= 24.99:
    classification = 'Peso Normal!'

elif bmi >= 25 and bmi <= 29.99:
    classification = 'Sobrepeso: Acima do peso ideal'

elif bmi >= 30 and bmi <= 34.99:
    classification = 'Obesidade Grau 1'

elif bmi >= 35 and bmi <= 39.99:
    classification = 'Obesidade Grau 2'

else:
    classification = 'Obesidade Grau 3'

print(f'{name} o seu IMC-Indice de Massa Corporal é igual a: {bmi}. O que lhe classifica como: {classification}!')