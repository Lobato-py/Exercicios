'''
# Minha resolução:
while True:
    primeiro_valor = input ('Digite um valor: ')
    segundo_valor = input('Digite outro valor: ')

    try:
        v1float = float(primeiro_valor)
        v2float = float(segundo_valor)

        if v1float > v2float:
            print(f"O primeiro valor({v1float}) é MAIOR que o segundo valor({v2float}).")
        
        elif v1float == v2float:
            print(f"Os dois valores são iguais.")
        
        elif v2float > v1float:
            print(f"O segundo valor({v2float}) é MAIOR que o primeiro valor({v1float})")

        break

    except ValueError:
        print('\nERRO: Por favor, digite um valor válido.\n ')
# Adicionei MUITA firula, fiz conversão de STR para Float; fiz um loop funcional caso o usuário digitasse algo com a intenção de
#quebrar meu código; compara em números Float, então, entende a diferença entre 10.5 e 7.3 por exemplo.
'''
'''
# Resoluçaõ do professor:
# ps: simples por conta que teoricamente estamos no começo do curso, eu que fico inventando firula

primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')
'''

# Brincando:

while True:
    try:
        v1 = float(input('Digite um valor: '))
        v2 = float(input('Digite outro valor: '))
        
        if v1 > v2:
            print(f"O primeiro valor({v1}) é MAIOR que o segundo valor({v2}).")
        elif v1 == v2:
            print(f"Os dois valores são iguais.")
        else:
            print(f"O segundo valor({v2}) é MAIOR que o primeiro valor({v1}).")
        
        break
    except ValueError:
        print('\nERRO: Por favor, digite um valor válido.\n')

# Código mais limpo, mesma coisa que a primeira resolução.