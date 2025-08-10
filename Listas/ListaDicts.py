# O código inicial era para se verificar uma senha e ter um limite de tentativas. Foi alterado para realizar uma verificação de código enviada por celular
# normamalmemte por SMS, ou pode ser por e-mail.

tentativas = 0
codigo_verificacao = '123321'  # Código enviado para o usuário

print("Um código de verificação foi enviado para seu celular")

while tentativas < 3:
    codigo = input('Digite o código de verificação: ')
    if codigo == codigo_verificacao:
        print('Verificação concluida!')
        break
    else:
        tentativas += 1
        if tentativas < 3:
            print(f'Código inválido. Restam {3 - tentativas} tentativa(s).')
        else:
            print('Número máximo de tentativas excedido. Acesso bloqueado.')