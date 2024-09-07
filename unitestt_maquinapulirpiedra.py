import unittest
from maquinapulirpiedra import maquinapulirpiedra

class TestMaquinaPulirPiedra(unittest.TestCase):

    def test_inicializacion(self):
        marmol = maquinapulirpiedra("marmol", "1")
        self.assertEqual(marmol.piedra, "marmol")
        self.assertEqual(marmol.pulido, "1")
        self.assertFalse(marmol.comenzado)

    def test_comenzar(self):
        marmol = maquinapulirpiedra("marmol", "1")
        marmol.comenzar()
        self.assertTrue(marmol.comenzado)

    def test_terminar(self):
        marmol = maquinapulirpiedra("marmol", "1")
        marmol.comenzar()
        marmol.terminar()
        self.assertFalse(marmol.comenzado)

if __name__ == "__main__":
    unittest.main()
























    