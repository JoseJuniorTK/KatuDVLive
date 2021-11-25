import pandas as pd


def mercadolivre(filename):

    #read the missing data - checking if there is a null
    missingvalue = ['?', '0', '--']
    my_file = pd.read_excel(filename, header=None, engine='openpyxl')
    df_data = pd.DataFrame(data=my_file)
    # Leitura inicial de dados
    df_data.drop(df_data.index[[0, 1, 2, 3, 4, 5, 6]], inplace=True)

    df_data.columns = df_data.iloc[0]
    df_data.drop(df_data.index[0], inplace=True)
    # df_data_final = df_data.groupby(['Número de venda', 'Título do anúncio', 'Data de venda', 'Preço unitário', 'Categoria do anúncio'], as_index=False).agg({'Valor da tarifa': 'sum'})
    df_data_final = df_data.filter(['Título do anúncio','Preço unitário'], axis=1)
    df_data_final = df_data_final.rename({'Título do anúncio': 'Info1', 'Preço unitário': 'Info2'}, axis=1)
    # df_data_final['Data de venda'] = pd.to_datetime(df_data_final['Data de venda']).dt.normalize()
    print(df_data_final)
    dfd3 = df_data_final.to_dict('r')
    
    return dfd3