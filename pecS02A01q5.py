valor_produto = float(input('Insira o valor do produto: '))
a_vista = valor_produto - (valor_produto * 9/100)
parcelado5_vezes = valor_produto / 5
parcelado10_vezes = (valor_produto / 10) + ((valor_produto * 17/100) / 10)
print(f'Pagando À vista seu produto fica no avlor de R${a_vista:.2f}.')
print(f'Pagando parcelado em até 5 vezes sem juros a parcela fica R${parcelado5_vezes:.2f}.')
print(f'Pagando parcelado em 10 vezes e com juros a parcela é de R${parcelado10_vezes:.2f}.')
