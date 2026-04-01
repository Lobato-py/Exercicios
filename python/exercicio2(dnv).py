# cálculo do IMC: peso corporal/altura*altura

# nome = 'Gustavo Lobato'
# altura = 1.70
# peso = 83
# imc = ... # os ... se chama "place holder", ele não quebra o código e roda normalmente (tem outras funções)

# Gustavo Lobato tem 1.70 de altura,
# pesa 83 quilos e seu IMC é:
# (insira o valor aqui) 


nome = input("Digite seu nome: ")
altura = input("Digite sua altura(exemplo: 1.86): ")
peso = input("Digite seu peso em KG: ")

altura_float= float(altura)
peso_float= float(peso)

imc= peso_float/(altura_float*altura_float)
# poderia ter feito "peso_float/altura_float ** 2"

print(f'{nome} tem {altura_float} de altura, pesa {peso_float} e seu IMC é: {imc}')
# adicionei mais firula do que deveria aqui, até porque a gente ainda não viu f-strings
# adicionei inputs também para ficar mais dinâmico para usuário