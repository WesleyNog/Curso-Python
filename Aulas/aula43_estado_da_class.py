class Camera():
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando
 
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando!')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def para_filmar(self):
            if not self.filmando:
                print(f'{self.nome} NÃO está filmando')
                return
            
            print(f'{self.nome} ESTÁ parando de Filmar')
            self.filmando = False
        

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} NÃO pode fotografar filmando')
            return

        print(f'{self.nome} está fotografando...')
        

    
c1 = Camera('Cannon')
c2 = Camera('Sony')
c1.filmar()
c1.filmar()
c1.fotografar()
c1.para_filmar()
c1.fotografar()

print()

c2.para_filmar()
c2.filmar()
c2.filmar()
c2.fotografar()
c2.para_filmar()
c2.fotografar()

