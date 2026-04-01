# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos.
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# Minha resolução exercício 1:
# errei a proposta :(

def conta():  
    multiplicador = input('Digite o multiplicador: ')
    multiplicador = int(multiplicador)

    multiplicando = input('Digite o multiplicando: ')
    multiplicando = int(multiplicando)

    resultado = multiplicando * multiplicador
    resultado = float(resultado)

    print(f'O resultado da multiplicação entre {multiplicador}x{multiplicando} é = {resultado}.')
    
conta()


# Minha resolução exercício 2:

def par_ou_impar():
    numero = input('Digite um número: ')
    numero = float(numero)

    if numero % 2 == 0:
        print(f'O número {numero} é par!')

    else:
        print(f'O número {numero} é ímpar!')

par_ou_impar()



# Resolução professor exercício 1:

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)
print(multiplicacao)

# Resolução professor exercício 2:

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0
    
    if multiplo_de_dois:
        return f'{numero} é par' # se caso nao for = 0, o valor vai se false
    return f'{numero} é ímpar' # logo, não precisa do else.


print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))