# Calculadora simples que fiz durante meu tempo livre no trabalho

while True:
    n1 = input('Digite um número: ')
    n2 = input('Digite outro número: ')
    op = input('Digite um operador ( + ; - ; * ; / ): ')

    try:
        # Tenta converter os inputs para float
        floatn1 = float(n1)
        floatn2 = float(n2)
        
        # Se a conversão der certo, o código continua aqui:
        if op == '+':
            print(f'{floatn1} + {floatn2} = {floatn1 + floatn2}')

        elif op == '-':
            print(f'{floatn1} - {floatn2} = {floatn1 - floatn2}')

        elif op == '*':
            print(f'{floatn1} * {floatn2} = {floatn1 * floatn2}')

        elif op == '/':
            if floatn2 != 0:
                print(f'{floatn1} / {floatn2} = {floatn1 / floatn2}')
            
            else:
                print("Erro: Divisão por zero não é permitida.")
        else:
            print("Operador inválido!")
        
        # O break sai do loop 'while' se tudo correr bem
        break

    except ValueError:
        # Se o float() falhar, ele cai aqui
        print("\nErro: Você não digitou um número válido. Tente novamente.\n")
