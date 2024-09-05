class MaquinaCremallera:
    def __init__(self):
        self.cintas_tejidas = 0
        self.cremalleras = 0

    def tejerCinta(self, cantidad):
        self.cintas_tejidas += cantidad
        print(f"{cantidad} cintas tejidas correctamente.")

    def fabricarCremallera(self, cantidad):
        self.cremalleras += cantidad
        print(f"{cantidad} cremalleras fabricadas correctamente.")
