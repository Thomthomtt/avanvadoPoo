'''class Pessoa():
    def __init__(self, peso, nome, idade):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.comendo=False
        self.falando=False
        self.dormindo=False
    def comer(self):
        if self.comendo == True:
            print(f"{self.nome}, já está comendo")
        elif self.falando==True:
            print(f"{self.nome} não pode comer porque está falando")
        elif self.dormindo==True:
            print(f"{self.nome} não pode comer porque está dormindo")
        else:
            print(f"{self.nome} está comendo")
            self.comendo=True
    def falar(self):
        if self.comendo == True:
            print(f"{self.nome} não pode falar porque está comendo")
        elif self.falando == True:
            print(f"{self.nome}, já está falando")
        elif self.dormindo == True:
            print(f"{self.nome} não pode falar porque está dormindo")
        else:
            print(f"{self.nome} está falando")
            self.falando = True
    def dormir(self):
        if self.dormindo == True:
            print(f"{self.nome} já está dormindo")
        elif self.falando == True:
            print(f"{self.nome} não pode dormir porque está falando")
        elif self.comendo == True:
            print(f"{self.nome} não pode dormir porque está comendo")
        else:
            print(f"{self.nome} está dormindo")
            self.dormindo = True
    def pararComer(self):
        if self.comendo==True:
            print(f"Parou de comer")
            self.comendo=False
        else:
            print(f"{self.nome} não ta comendo")

    def pararDormir(self):
        if self.dormindo == True:
            print(f"Parou de dormir")
            self.dormindo =False
        else:
            print(f"{self.nome} não tá dormindo")

    def pararFalar(self):
        if self.falando == True:
            print(f"Parou de falar")
            self.falando =False
        else:
            print(f"{self.nome} não tá falando")'''
class ContaBancaria():
    def __init__(self, nome, numero, tipo):
        self.nome=nome
        self.numero=numero
        self.tipo=tipo
        self.saldo=0
        self.status=False
        self.limite=0
    def depositar(self, deposito):
        if self.status==False:
            print(f"Sua conta não está ativa, você precisa ativar!")
        else:
            self.saldo+=deposito
            print(f"Deposito no valor de {deposito:.2f} efetuado com sucesso!")
    def sacar(self, saque):
        if self.status==False:
            print(f"Sua conta não está ativa, você precisa ativar!")
        else:
            if (self.saldo+self.limite)<saque:
                print(f"Saldo Indisponivel. Saque no valo de {saque} não é possível!")
            else:
                self.saldo-=saque
                print(f"Saque efetuado com sucesso no valor de {saque:.2f}!")
    def ativarConta(self):
        if self.status==False:
            self.status=True
            print(f"Parabéns {self.nome}, sua conta está ativada!")
        else:
            print("Sua conta já está ativada!")
    def verificarSaldo(self):
        if self.status==False:
            print(f"Sua conta não está ativa, você precisa ativar!")
        else:
            print(f"O saldo da sua conta é: {self.saldo:.2f}")
    def novoLimite(self, limite):
        if self.status==False:
            print(f"Sua conta não está ativa, você precisa ativar!")
        else:
            self.limite+=limite
            print(f"Seu novo limite é: {self.limite}")