import unittest
from maquina_cremallera import MaquinaCremallera


class TestMaquinaCremallera(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaCremallera("maq1")

    def test_es_clase(self):
        # Éste test verifica que la variable maquina es una instancia de la clase MaquinaCremallera
        maquina = MaquinaCremallera("maq1")
        self.assertIsInstance(maquina, MaquinaCremallera)

    def test_tejer_cinta(self):
        # Éste test verifica que la función tejerCinta() incrementa el atributo cintas_tejidas
        self.maquina.tejerCinta(10)
        self.assertEqual(self.maquina.cintas_tejidas, 10)

    def test_fabricar_cremallera(self):
        # Éste test verifica que la función fabricarCremallera() incrementa el atributo cremalleras
        self.maquina.tejerCinta(10)
        self.maquina.fabricarCremallera()
        self.assertEqual(self.maquina.cremalleras, 10)

    def test_tenir(self):
        # Éste test verifica que la función teñir() "tiñe" las cremalleras y cintas y decrementa cintas_tejidas y cremalleras
        self.maquina.tejerCinta(10)
        self.maquina.fabricarCremallera()
        self.maquina.teñir("rojo")
        self.assertEqual(self.maquina.cremalleras_teñidas, 10)
        self.assertEqual(self.maquina.cintas_tejidas, 0)
        self.assertEqual(self.maquina.cremalleras, 0)

    def test_fabricar_cremallera_completa(self):
        # Éste test verifica que la función fabricarCremalleraCompleta() realiza todas las operaciones necesarias para fabricar un numero de cremalleras
        self.maquina.fabricarCremalleraCompleta(10, "rojo")
        self.assertEqual(self.maquina.cremalleras_empaquetadas, 10)

    def test_len(self):
        # Éste test verifica que el método __len__() retorna la cantidad de cremalleras empaquetadas
        self.assertEqual(len(self.maquina), 0)

        self.maquina.fabricarCremalleraCompleta(10, "azul")
        self.assertEqual(len(self.maquina), 10)

        self.maquina.fabricarCremalleraCompleta(5, "azul")
        self.assertEqual(len(self.maquina), 5)


if __name__ == "__main__":
    unittest.main()
