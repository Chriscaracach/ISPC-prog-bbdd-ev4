class MaquinaCremallera:
    def __init__(self):
        self.cintas_tejidas = 0
        self.cremalleras = 0
        self.cremalleras_teñidas = 0
        self.cremalleras_empaquetadas = 0

    def tejerCinta(self, cantidad):
        self.cintas_tejidas += cantidad
        print(f"{cantidad} cintas tejidas correctamente.")

    def fabricarCremallera(self, cantidad):
        self.cremalleras += cantidad
        print(f"{cantidad} cremalleras fabricadas correctamente.")

    def teñir(self, color):
        if not self.cintas_tejidas or not self.cremalleras:
            print(
                "Es necesario tener cintas tejidas y cremalleras para poder teñirlas. Por favor, primero teje cintas y fabrica cremalleras."
            )
        else:
            minimo = min(self.cremalleras, self.cintas_tejidas)
            self.cremalleras_teñidas = minimo
            self.cintas_tejidas -= minimo
            self.cremalleras -= minimo
            print(
                f"Todas las cremalleras fueron teñidas correctamente de color {color}."
            )

    def empaquetar(self):
        if not self.cremalleras_teñidas:
            print(
                "Error. Las cremalleras deben estar teñidas para poder ser empaquetadas."
            )
        else:
            self.cremalleras_empaquetadas = self.cremalleras_teñidas
            self.cremalleras_teñidas = 0
            print("Cremalleras empaquetadas correctamente.")

    def fabricarCremalleraCompleta(self, cantidad, color):
        self.tejerCinta(cantidad)
        self.fabricarCremallera(cantidad)
        self.teñir(color)
        self.empaquetar()
        print(f"{cantidad} cremalleras de color {color} fabricadas correctamente.")

    def __len__(self):
        return self.cremalleras_empaquetadas
