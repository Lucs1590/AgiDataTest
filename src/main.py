import pandas as pd
import numpy as np


def minha_funcao(dados: pd.DataFrame, status_resposta: str) -> pd.DataFrame:
    """ # Minha Função
    Função para calculo de grupo, quantidade de registros de cada
     grupo e a taxa de resposta.

    Args:
        dados (pd.DataFrame): Dataframe com grupos e resposta se
         foi contratado ou não;
        status_resposta (str): String para filtro de contratação.

    Raises:
        TypeError: Erro devido a inserção de valor que não é string
         no segundo parâmetro.

    Returns:
        pd.DataFrame: Dataframe com grupos, quantidade e taxa de
         resposta calculada.
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
    Essa é a função responsável por chamar a `minha_funcao` e definir a ordem
     do código.
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
    df_positivo = minha_funcao(bank_df, status_resposta="S")
    df_negativo = minha_funcao(bank_df, status_resposta="N")
    print('\n{}\n'.format(df_positivo))
    print('\n{}\n'.format(df_negativo))


if __name__ == '__main__':
    main()
