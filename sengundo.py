#	Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em todas as suas paredes (considere que não será descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1.5 m2. #



comprimento = float(input('informe o comprimento da cozinha:'))
largura = float( input('input alargura da cozinha:'))
altura = float(input('informe a altura da cozinha:'))
area_parede = 2* largura *(comprimento + altura)
caixas = area_parede / 1.5
print(f'a quantidade de caixas de azuleijos nessesario e de { caixas} ')