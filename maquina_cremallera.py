class MaquinaCremallera:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cintas_tejidas = 0
        self.cremalleras = 0
        self.cremalleras_teñidas = 0
        self.cremalleras_empaquetadas = 0

    def tejerCinta(self, cantidad):
        self.cintas_tejidas += cantidad
        print(f"{cantidad} cintas tejidas correctamente.")

    def fabricarCremallera(
        self,
    ):
        if not self.cintas_tejidas:
            print(
                "Es necesario tener cintas tejidas para poder fabricar cremalleras. Por favor, primero teje cintas."
            )
        else:
            self.cremalleras = self.cintas_tejidas
            self.cintas_tejidas = 0
            print(f"{self.cremalleras} cremalleras fabricadas correctamente.")

    def teñir(self, color):
        if not self.cremalleras:
            print(
                "Es necesario tener cremalleras fabricadas para poder teñirlas. Por favor, primero fabrica cremalleras."
            )
        else:
            self.cremalleras_teñidas = self.cremalleras
            self.cremalleras = 0
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
        self.fabricarCremallera()
        self.teñir(color)
        self.empaquetar()
        print(f"{cantidad} cremalleras de color {color} fabricadas correctamente.")

    def visualizarDatos():
        print(f"Cintas tejidas: {self.cintas_tejidas}")
        print(f"Cremalleras fabricadas: {self.cremalleras}")
        print(f"Cremalleras teñidas: {self.cremalleras_teñidas}")
        print(f"Cremalleras empaquetadas: {self.cremalleras_empaquetadas}")

    def __len__(self):
        return self.cremalleras_empaquetadas
