class Car:
    def __init__(self, name) -> None:
        self.name = name
        self._motor = None
        self._fab = None

    @property
    def motor(self):
        return self._motor
        
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fab(self):
        return self._fab
        
    @fab.setter
    def fab(self, valor):
        self._fab = valor


class Fabricante:
    def __init__(self, name) -> None:
        self.name = name


class Motor:
    def __init__(self, name) -> None:
        self.name = name



corolla = Car('Corolla')
toyota = Fabricante('Toyota')
hybrid_1_8 = Motor('Hydrid 1.8')
corolla.fab = toyota
corolla.motor = hybrid_1_8

print(corolla.name, corolla.fab.name, corolla.motor.name)

argo = Car('Argo')
fiat = Fabricante('Fiat')
fire_1_6 = Motor('Fire 1.6')
argo.fab = fiat
argo.motor = fire_1_6

print(argo.name, argo.fab.name, argo.motor.name)

fusion = Car('Fusion')
ford = Fabricante('Ford')
fusion.fab = ford
corolla.motor = hybrid_1_8
print(fusion.name, fusion.fab.name, corolla.motor.name)