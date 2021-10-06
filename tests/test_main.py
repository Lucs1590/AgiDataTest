import unittest
import numpy as np
import pandas as pd

import src.main as main


class TestFunctionUnit(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(np.array([
            ['Grupo A', 'S'],
            ['Grupo A', 'S'],
            ['Grupo A', 'S'],
            ['Grupo A', 'S'],
            ['Grupo A', 'N'],
            ['Grupo A', 'N'],
            ['Grupo A', 'N'],
            ['Grupo A', 'N'],
            ['Grupo B', 'S'],
            ['Grupo B', 'S'],
            ['Grupo B', 'S'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
            ['Grupo B', 'N'],
        ]), columns=['covariavel', 'contratou'])

    def test_minha_funcao_tipos(self):
        with self.assertRaises(TypeError):
            main.minha_funcao(self.df, 1)

    def test_minha_funcao_retorno_S(self):
        ...

    def test_minha_funcao_retorno_N(self):
        ...

    def test_minha_funcao_tamanho(self):
        ...


if __name__ == '__main__':
    unittest.main()
