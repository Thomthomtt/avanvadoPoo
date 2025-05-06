class Pessoa():
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
            print(f"{self.nome} não tá falando")


