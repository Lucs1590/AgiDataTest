import pandas as pd
import numpy as np


def minha_funcao(dados: pd.DataFrame, status_resposta: str) -> pd.DataFrame:
    """ # Minha Funcao
     Function to calculate group, number of records for each
      group and the response rate.

     Args:
        data (pd.DataFrame): Dataframe with groups and answer if
          was hired or not;
        response_status (str): String for hiring filter.

     Raises:
        TypeError: Error due to insertion of non-string value
          in the second parameter.

     Returns:
        pd.DataFrame: Dataframe with groups, numb. of register
         and rate of calculated answer.
    """
    if (not isinstance(status_resposta, str)):
        raise TypeError('invalid input, try to send a string with "S" or "N".')

    df = dados.groupby('covariavel').count()
    df['taxa_resposta'] = (dados[(dados.contratou == status_resposta)].groupby(
        'covariavel'
    ).count() / dados.groupby('covariavel').count()).contratou.to_list()
    df = df.rename(columns={"contratou": "n"})
    return df.reset_index()


def main():
    """ # Main
     This is the function responsible for calling `minha_funcao` and defining
      the code order.
    """
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
    positive_df = minha_funcao(bank_df, status_resposta="S")
    negative_df = minha_funcao(bank_df, status_resposta="N")
    print('\n{}\n'.format(positive_df))
    print('\n{}\n'.format(negative_df))


if __name__ == '__main__':
    main()
