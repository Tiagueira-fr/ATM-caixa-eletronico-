
## Aqui definimos os aspectos do titular do cartao

class titularCartao():
    def __init__(self, numCartao , pin , nome, sobrenome, saldo):
        self.numCartao = numCartao
        self.pin = pin
        self.nome = nome
        self.sobrenome = sobrenome
        self.saldo = saldo


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
    

    ## Output da info do titular
    def print_out(self):
        print("Titular : " , self.nome , self.sobrenome)
        print("Cartao : " , self.numCartao)
        print("Senha / Pin : " , self.pin)
        print("Saldo disponivel : " , self.saldo)