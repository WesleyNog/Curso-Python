class Cliente:
    def __init__(self, name) -> None:
        self.name = name
        self.adresses = []

    def insert_adress(self, adress, number):
        self.adresses.append(Adress(adress, number))

    def list_adress(self):
        for adress in self.adresses:
            print(adress.adress, adress.number)

    

class Adress:
    def __init__(self, adress, number) -> None:
        self.adress = adress
        self.number = number


cliente = Cliente('Wesley')
cliente.insert_adress('Sulamita Portela', 30)
cliente.insert_adress('Rua 3', 177)

cliente.list_adress()