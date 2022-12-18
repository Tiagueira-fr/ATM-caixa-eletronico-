# Aqui configuramos o console do Caixa Eletronico
from titularCartao import titularCartao

## Menu Inicial
def show_menu():
    print("Escolha uma das opcoes abaixo para continuar: ")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Revelar Saldo")
    print("4. Nova Senha")
    print("5. Encerrar")


## Efetua o deposito, op 1

def deposito(titularCartao):
    try:
        deposito = float(input("Insira o valor a ser depositado: "))
        titularCartao.set_saldo(titularCartao.get_saldo() + deposito)

        print("Transacao efetuada, saldo atual: ", str(titularCartao.get_saldo()))

    except:
        print("Valor Invalido")
   
    """
    Esta função permite que o usuário efetue um depósito na sua conta.
    Ela recebe como parâmetro o objeto titularCartao, que é a conta do usuário, 
    e solicita o valor do depósito. Se o valor for válido, o saldo da conta é atualizado e 
    exibido para o usuário. Caso contrário, uma mensagem de erro é exibida.
    """


## Efetua o saque, op 2
def saque(titularCartao):
    try:
        saque = float(input("Insira o valor a ser sacado: "))
        if(titularCartao.get_saldo() < saque):
            print("Saldo insuficiente!")
        else:
            titularCartao.set_saldo(titularCartao.get_saldo() - saque)
            print("Saque efetuado, seu novo saldo e de: " , str(titularCartao.get_saldo()))
    except:
        print("Valor Invalido")
    
    """
    Esta função permite que o usuário efetue um saque da sua conta.
    Ela recebe como parâmetro o objeto titularCartao, que é a conta do usuário, 
    e solicita o valor do saque. Se o valor for válido e o saldo da conta for suficiente, 
    o saldo é atualizado e exibido para o usuário. Caso contrário, uma mensagem de erro é exibida.
    """


## Revela Saldo, op 3
def revelaSaldo(titularCartao):
    print("Seu saldo e de: " , str(titularCartao.get_saldo()))
"""
    Esta função exibe o saldo atual da conta do usuário.
    Ela recebe como parâmetro o objeto titularCartao, que é a conta do usuário, 
    e exibe o saldo para o usuario
"""

## Muda a senha, op 4
def novaSenha(titularCartao):
    
    novaSenha = int(input("\nA sua nova senha deve ter 4 digitos.\nDigite a nova senha: ").strip())

    # Conta quantos dígitos a nova senha tem
    contador = 0
    while novaSenha > 0:
        novaSenha = novaSenha // 10
        contador += 1

    # Verifica se a nova senha é válida
    if user_atual.get_pin() != novaSenha and contador <= 4 :
        confirmaSenha = int(input("Confirme a senha: ").strip())
        
        # Verifica se a nova senha é igual à senha atual
        if (novaSenha == user_atual.get_pin()):
            print("O novo PIN / Senha deve ser diferente da atual")
        
        # Verifica se a nova senha foi confirmada corretamente
        if (novaSenha == confirmaSenha):     
             titularCartao.set_pin (novaSenha)
        elif (novaSenha == user_atual.get_pin()):
             print("O novo PIN / Senha deve ser diferente da atual")
        else:
            # Enquanto as senhas não forem iguais, solicita novas senhas para o usuário
            while (True):
                confirmaSenha = int(input("As Senhas não batem, tente novamente: ").strip())
                if novaSenha == confirmaSenha:
                    titularCartao.set_pin(novaSenha)
                    break
                
    else:
        print("O novo PIN / Senha deve ser diferente da atual, e tambem deve ter no maximo 4 digitos\n")
        
    
    """
    Esta função permite que o usuário altere a senha de sua conta.
    Ela recebe como parâmetro o objeto titularCartao, que é a conta do usuário, 
    e solicita a nova senha. A nova senha deve ter no máximo 4 dígitos e ser diferente da senha atual.
    Se a nova senha for válida, ela é confirmada pelo usuário e, se as duas senhas digitadas forem iguais,
    a senha da conta é atualizada. Caso contrário, uma mensagem de erro é exibida.
    """

## Revela Informação, op 99 oculta apenas para caso de teste
def infoUser(titularCartao):
    print(titularCartao.print_out())
    """
    Esta funçao é utilizada para revelar todas as informacoes do usuario, esta oculta no menu principal.
    Ela recebe como parametro o objeto titularCartao, que é a conta do usuario.
    """

## Inicializa o usuario no console
if __name__ == "__main__":
    user_atual = titularCartao("" , "" , "" , "" , "" , "")

    ## DB dos titulares
    list_titulares = []
    list_titulares.append(titularCartao("123321" , 1234 , "Maria" , "Aparecida" , 200.00 , 0))
    list_titulares.append(titularCartao("134431" , 4321 , "Celio" , "Costa" , 2000.21 , 0))
    list_titulares.append(titularCartao("101202" , 1357 , "Neymar" , "Junior" , 18.00 , 0))
    list_titulares.append(titularCartao("303404" , 1013 , "Rafael" , "Garcia" , 165.51 , 0))
    list_titulares.append(titularCartao("404505" , 2468 , "Leticia" , "Nominato" , 58290.30 , 0))

    ## Inicia o usuario com o numero do cartao de debito
    debito_numCartao = ""
    while True:
        try:
            debito_numCartao = input("Insira o numero do cartao: ")
            match_numCartao = [titular for titular in list_titulares if titular.numCartao == debito_numCartao]

            ## Loop breack
            if (len(debito_numCartao) > 0):
                user_atual = match_numCartao[0]
                break
            else:
                print("Numero do cartao nao reconhecido. Tente novamente:")  

        except:
            print("Numero do cartao nao reconhecido. Tente novamente:")

    ## Inicia o usuario com a Senha / Pin
    while True:
        try:
            userPin = int(input("Insira a sua Senha / Pin: ").strip())
            
            ## Loop breack
            if(user_atual.get_pin() == userPin):
                break
            else:
                print("Senha / Pin invalida! Por favor tente de novo")
        except:
            print("Senha / Pin invalida! Por favor tente de novo")

    ## Inicia o menu
    
    # Verifica o sistema operacional do usuario
    import os
    import platform
    try: 
        system = platform.system()
        print(system)
            # Limpa a tela em sistemas Unix
        if system == "Linux":    
            os.system("clear")
        
        elif system == "Windows":
            # Limpa a tela em sistemas Windows
            os.system("cls")
        
        elif system == "Darwin":
            os.system("clear")
    # Trata erro caso o sistema operacional não seja reconhecido
    except:
        None
        
    print("\nBem vindo(a)" , user_atual.get_nome(), " :)")

    opcao = 0

    while(True):
        show_menu()
        try:
            opcao = int(input())

        except:
            print("\nOpcao invalida. Tente novamente")

        
        if (opcao == 1):
            deposito(user_atual)

        elif(opcao == 2):
            saque(user_atual)

        elif(opcao == 3):
            revelaSaldo(user_atual)
        
        elif(opcao == 4):
            novaSenha(user_atual)

        elif(opcao == 5):
            break

        elif(opcao == 99):
            infoUser(user_atual)
        
        else:
            opcao = 0 
            print("\nObrigado por me testar")
        
        