# Criação de um objeto SimpleImputer
from sklearn.impute import SimpleImputer
import numpy as np

def Missing_Value_imputer():

    imputer = SimpleImputer(
        missing_values=np.nan,  # os valores faltantes são do tipo np.nan (padrão Pandas)
        strategy='constant',  # a estratégia escolhida é a alteração do valor faltante por uma constante
        fill_value=0,  # a constante que será usada para preenchimento dos valores faltantes é um int64=0.
        verbose=0,
        copy=True
    )

    return imputer

# print(Missing_Value_imputer())
