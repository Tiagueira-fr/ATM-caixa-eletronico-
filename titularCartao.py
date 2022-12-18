
## Aqui definimos os aspectos do titular do cartao

class titularCartao():
    def __init__(self, numCartao , pin , nome, sobrenome, saldo , credito):
        self.numCartao = numCartao
        self.pin = pin
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo
        self.credito = credito


    ## Usa metodos
    def get_numCartao(self):
        return self.numCartao
    
    def get_pin(self):
        return self.pin
    
    def get_nome(self):
        return self.nome
    
    def get_sobrenome(self):
        return self.sobrenome
    
    def get_saldo(self):
        return self.saldo
    
    def get_credito(self):
        return self.credito
    
    def pagar_fatura(self, valor):
        self.saldo += valor

    def fazer_compra(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        elif valor <= self.saldo + self.credito:
            self.saldo = 0
            self.credito -= (valor - self.saldo)
        else:
            raise ValueError("Saldo e crédito insuficientes")


    ## Atualiza metodos
    def set_numCartao(self, novoVal):
        self.numCartao = novoVal
    
    def set_pin(self, novoVal):
        self.pin = novoVal
    
    def set_nome(self, novoVal):
        self.nome = novoVal
    
    def set_sobrenome(self, novoVal):
        self.sobrenome = novoVal
    
    def set_saldo(self, novoVal):
        self.saldo = novoVal
    
    def set_credito(self, novoVal):
        self.credito = novoVal
    
    ## Validacoes a serem implementadas



    ## Output da info do titular
    def print_out(self):
        print("Titular : " , self.nome , self.sobrenome)
        print("Cartao : " , self.numCartao)
        print("Senha / Pin : " , self.pin)
        print("Saldo disponivel : " , self.saldo)
        print ("Credito disponivel para uso: " , self.credito)


    
"""
    def set_numCartao(self, novoVal):
        if len(novoVal) == 16 and all(c.isdigit() for c in novoVal):
            self.numCartao = novoVal
        else:
             raise ValueError("Número de cartão inválido")

    def set_pin(self, novoVal):
        num_digitos = str(novoVal)
        if len(num_digitos) >= 4 and all(c.isdigit() for c in novoVal):
            self.pin = novoVal
        else:
            raise ValueError("PIN inválido")

"""