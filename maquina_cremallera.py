class MaquinaCremallera:
    def __init__(self):
        self.cremalleras = 0

    def tejerCinta(self, cantidad):
        self.cintas_tejidas += cantidad
        print(f"{cantidad} cintas tejidas correctamente.")
