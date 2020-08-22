# Criação de um objeto SimpleImputer
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
import numpy as np

def Missing_Value_imputer():

    imputer = KNNImputer(
        n_neighbors=5
        ,missing_values=np.nan  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
        ,copy=True
    )

    return imputer

'''
# print(Missing_Value_imputer())
from sklearn.impute import KNNImputer
imputer = KNNImputer(
    n_neighbors=5
    ,missing_values=np.nan  # os valores faltantes são do tipo ``np.nan`` (padrão Pandas)
    ,copy=True
    )

imputer = SimpleImputer(
        missing_values=np.nan,  # os valores faltantes são do tipo np.nan (padrão Pandas)
        strategy= ,  # a estratégia escolhida é a alteração do valor faltante por uma constante
        fill_value=0,  # a constante que será usada para preenchimento dos valores faltantes é um int64=0.
        verbose=0,
        copy=True
    )
'''
