peso = float(input('Qual é o seu peso? (KG): '))
altura = float(input('Qual a sua Altura? (m): '))

imc = peso / (altura ** 2)

print(f'O IMC desta pessoa é de {imc:.2f}')

if imc < 18.5:
    print('Você está ABAIXO do peso ideal.')
elif 18.5 <= imc < 25:
    print('Você está DENTRO DO PESO IDEAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc <40:
    print('Você está em OBESIDADE, cuidado!')
elif imc >= 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

#Este programa foi desenvolvido com fins de cálculo do ICM (Indíce de Massa Corporal).
#O programa permitirá e irá:
# #O usuário inserir os valores de seu peso e altura.
#Calcular o valores informando o valor de ICM referente aos valores inseridos.
#Retornar uma mensagem para o usuário se o mesmo se encontra abaixo do peso, no peso ideal, sobrepeso, obesidade e obesidade mórbida.