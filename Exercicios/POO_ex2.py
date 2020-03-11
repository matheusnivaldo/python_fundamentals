class Ave():
    def __init__(self):
        self.penas = True
        self.asas = 2
        self.bico = True
        self.patas = 2
        self.rabo = True
        self.olhos = 2

    def voar(self):
        print('Ave voando')
    
    def pousar(self):
        print('Pousando')

    def dormir(self):
        print('Dormindo')

    def comer(self):
        print('Comendo Alpiste')

# Faça uma classe sabia que herde caracteristicas do Passaro
# e as use
# Faça uma galinha que herde caracteristicas de Passo
# e mantenha as suas

class Sabia(Ave):
    def cantar(self):
        print("Cantando")

    def pousar(self):
        print('Sabia Pousando')

    def dormir(self):
        print('Sabia Dormindo')

    def comer(self):
        print('Sabia Comendo Alpiste')

sabino = Sabia()
sabino.voar()
sabino.pousar()
sabino.comer()


class Galinha(Ave):
    def __init__(self):
        self
    
    def voar(self):
        print("Galinha nem pode voar")

    def comer(self):
        print("Comendo milho")

carijo = Galinha()
carijo.voar()
carijo.comer()
carijo.dormir()