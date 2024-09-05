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
