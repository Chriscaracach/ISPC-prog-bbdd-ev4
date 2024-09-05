import unittest
from maquina_cremallera import MaquinaCremallera


class TestMaquinaCremallera(unittest.TestCase):

    def setUp(self):
        self.maquina = MaquinaCremallera()

    def test_es_clase(self):
        # Éste test verifica que la variable maquina es una instancia de la clase MaquinaCremallera
        maquina = MaquinaCremallera()
        self.assertIsInstance(maquina, MaquinaCremallera)

    def test_tejer_cinta(self):
        self.maquina.tejerCinta(10)
        self.assertEqual(self.maquina.cintas_tejidas, 10)

    def test_fabricar_cremallera(self):
        self.maquina.fabricarCremallera(15)
        self.assertEqual(self.maquina.cremalleras, 15)

    def test_tenir(self):
        self.maquina.tejerCinta(10)
        self.maquina.fabricarCremallera(10)
        self.maquina.teñir("rojo")
        self.assertEqual(self.maquina.cremalleras_teñidas, 10)
        self.assertEqual(self.maquina.cintas_tejidas, 0)
        self.assertEqual(self.maquina.cremalleras, 0)

    def test_fabricar_cremallera_completa(self):
        self.maquina.fabricarCremalleraCompleta(10, "rojo")
        self.assertEqual(self.maquina.cintas_tejidas, 10)
        self.assertEqual(self.maquina.cremalleras, 10)
        self.assertEqual(self.maquina.cremalleras_teñidas, 10)


if __name__ == "__main__":
    unittest.main()
