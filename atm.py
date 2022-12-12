## Aqui configuramos o console do Caixa Eletronico

from titularCartao import titularCartao

## Menu Inicial
def show_menu():
    print("Escolha uma das opcoes abaixo para continuar: ")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Revelar Saldo")
    print("4. Finalizar")


## Efetua o deposito, op 1
def deposito(titularCartao):
    try:
        deposito = float(input("Insira o valor a ser depositado: "))
        titularCartao.set_saldo(titularCartao.get_saldo() + deposito)

        print("Transacao efetuada, saldo atual: ", str(titularCartao.get_saldo()))

    except:
        print("Valor Invalido")


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


## Revela Saldo, op 3
def revelaSaldo(titularCartao):
    print("Seu saldo e de: " , str(titularCartao.get_saldo()))

## Inicializa o usuario no console
if __name__ == "__main__":
    user_atual = titularCartao("" , "" , "" , "" , "")

    ## DB dos titulares
    list_titulares = []
    list_titulares.append(titularCartao("123321" , 1234 , "Maria" , "Aparecida" , 200.00))
    list_titulares.append(titularCartao("134431" , 4321 , "Celio" , "Costa" , 2000.21))
    list_titulares.append(titularCartao("101202" , 1357 , "Neymar" , "Junior" , 18.00))
    list_titulares.append(titularCartao("303404" , 1013 , "Rafael" , "Garcia" , 20000.51))
    list_titulares.append(titularCartao("404505" , 2468 , "Leticia" , "Nominato" , 165.30))

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

    print("Bem vindo " , user_atual.get_nome(), " :)")

    opcao = 0

    while(True):
        show_menu()
        try:
            opcao = int(input())

        except:
            print("Opcao invalida. Tente novamente")

        
        if (opcao == 1):
            deposito(user_atual)

        elif(opcao == 2):
            saque(user_atual)

        elif(opcao == 3):
            revelaSaldo(user_atual)
        
        elif(opcao == 4):
            break
        
        else:
            opcao = 0 
            print("Obrigado por me testar")
        
        