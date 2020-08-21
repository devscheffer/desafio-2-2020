import pandas as pd

'''
# Todo: classe nao esta funcionando
class cls_Convert:
    def __init__(self, df, df_key):
        self.df = df
        self.df_key = df_key

    # Mudar variavel categorica para numerica
    def convert_cat_to_num(self):
        self.df[self.df_key] = pd.factorize(self.df[self.df_key], sort=True)[0] + 1

    # Mudar variavel numerica para categorica
    def convert_num_to_cat(self, cat_num, cat_label):
        self.df[self.df_key].replace(to_replace=cat_num, value=cat_label, inplace=True)

'''
# Function
# Mudar variavel categorica para numerica
def convert_cat_to_num(df,df_key):
    df[df_key] = pd.factorize(df[df_key],sort=True)[0] + 1
    return df

# Mudar variavel numerica para categorica
def convert_num_to_cat(df,df_key,cat_num,cat_label):
    df[df_key].replace(to_replace = cat_num, value =cat_label, inplace=True)
    return df
    # Default values
# df_key = 'PERFIL'
# cat_num = [1,2,3,4,5]
# cat_label = [
#             'DIFICULDADE'
#             ,'EXATAS'
#             ,'EXCELENTE'
#             ,'HUMANAS'
#             ,'MUITO_BOM'
#         ]
