import pandas as pd
import numpy as np


def minha_funcao(dados, status_resposta: str):
    if (not isinstance(status_resposta, str)):
        raise TypeError('invalid input, try to send a string with "S" or "N".')


def main():
    data = np.array([
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
    ])
    bank_df = pd.DataFrame(data, columns=['covariavel', 'contratou'])
    df_positivo = minha_funcao(bank_df, status_resposta="S")
    df_negativo = minha_funcao(bank_df, status_resposta="N")


if __name__ == '__main__':
    main()
