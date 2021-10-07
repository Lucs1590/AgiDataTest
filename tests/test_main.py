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

    def test_wrong_param(self):
        with self.assertRaises(TypeError):
            main.minha_funcao(self.df, 1)

    def test_return_type(self):
        df = main.minha_funcao(self.df, "S")
        self.assertIsInstance(df, pd.DataFrame)

    def test_positive_hiring(self):
        df = main.minha_funcao(self.df, "S")
        self.assertEqual(df.values.tolist(), [
                         ['Grupo A', 8, 0.5], ['Grupo B', 10, 0.3]])

    def test_negative_hiring(self):
        df = main.minha_funcao(self.df, "N")
        self.assertEqual(df.values.tolist(), [
                         ['Grupo A', 8, 0.5], ['Grupo B', 10, 0.7]])

    def test_return_lenght(self):
        df = main.minha_funcao(self.df, "N")
        self.assertEqual(len(df.index), 2)


if __name__ == '__main__':
    unittest.main()
