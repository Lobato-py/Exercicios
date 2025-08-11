# Exercícios 
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.



# Minha resolução:

def multi_2 (*args):
   multiplicador = 2
   for numero in args:
      multiplicador *= numero
      return multiplicador
   
multiplicando = int(input('Digite um número para ser múltiplicado: '))


resultadox2 = multi_2(multiplicando)
print (f'Seu número multiplicado por 2 é igual à {resultadox2}.')
# resultadox2 = multi_2(10)

# print(resultadox2)

def multi_3 (*args):
   multiplicador = 3
   for numero in args:
      multiplicador *= numero
      return multiplicador
   
resultadox3 = multi_3(multiplicando)
print (f'Seu número multiplicado por 3 é igual à {resultadox3}.')

def multi_4 (*args):
   multiplicador = 4
   for numero in args:
      multiplicador *= numero
      return multiplicador
   
resultadox4 = multi_4(multiplicando)
print(f'Seu número multiplicado por 4 é igual à {resultadox4}.')

# Resolução do professor:

# def duplicar(numero):
#    return numero * 2


# def triplicar(numero):
#    return numero * 3


# def quadruplicar(numero):
#    return numero * 4

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)


print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))