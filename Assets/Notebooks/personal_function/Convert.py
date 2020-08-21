# Mudar variavel categorica para numerica
def convert_cat_to_num(df,df_key):
    df[df_key] = pd.factorize(df[df_key],sort=True)[0] + 1
    return df

# Mudar variavel numerica para categorica
def convert_num_to_cat(df,df_key,cat_bin,cat_label):
    df[df_key].replace(to_replace = cat_bin, value =cat_label, inplace=True)
    return df

# Default values
# df_key = 'PERFIL'
# cat_bin = [1,2,3,4,5]
# cat_label = [
#             'DIFICULDADE'
#             ,'EXATAS'
#             ,'EXCELENTE'
#             ,'HUMANAS'
#             ,'MUITO_BOM'
#         ]
