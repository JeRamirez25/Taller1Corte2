class IEstrategia:
    def ejecutar(self):
        pass

class Soldados(IEstrategia):
    def ejecutar(self):
        print("El soldado avanzo 3 posiciones y se resbala.")

class Arqueros(IEstrategia):
    def ejecutar(self):
        print("El arquero retrocede 1 posicion y dispara 2 flechas.")

class Caballeros(IEstrategia):
    def ejecutar(Self):
        print("El caballero avanza 5 posiciones y ataca con su espada.")

class Juego:
    def __init__(self, jugar : IEstrategia) -> None:
        self.jugar = jugar
    
    def ejecutar_juego(self):
        self.jugar.ejecutar()

class Usuario1(Juego):
    def __init__(self, jugar: IEstrategia) -> None:
        super().__init__(jugar)

if __name__ == "__main__":
    eleccion = int(input("Escoja el personaje con el que quiere jugar. \n"
    + "1. Soldado. \n"
    + "2. Arquero. \n"
    + "3. Caballero. \n"
    + "Digita tu personaje: "))
    if eleccion == 1:
        figura = Soldados()
    elif eleccion == 2:
        figura = Arqueros()
    elif eleccion == 3:
        figura = Caballeros()
    else:
        exit()
    usuario1 = Usuario1(figura)
    usuario1.ejecutar_juego()
