#%%

import pandas as pd

#%%

#%%
df01 = pd.read_csv('..\\Data\\raw\\Janeiro-divvy-tripdata.csv')
df02 = pd.read_csv('..\\Data\\raw\\Fevereiro-divvy-tripdata.csv')
df03 = pd.read_csv('..\\Data\\raw\\Marco-divvy-tripdata.csv')
df04 = pd.read_csv('..\\Data\\raw\\Abril-divvy-tripdata.csv')
df05 = pd.read_csv('..\\Data\\raw\\Maio-divvy-tripdata.csv')
df06 = pd.read_csv('..\\Data\\raw\\Junho-divvy-tripdata.csv')
df07 = pd.read_csv('..\\Data\\raw\\Julho-divvy-tripdata.csv')
df08 = pd.read_csv('..\\Data\\raw\\Agosto-divvy-tripdata.csv')
df09 = pd.read_csv('..\\Data\\raw\\Setembro-divvy-tripdata.csv')
df10 = pd.read_csv('..\\Data\\raw\\Outubro-divvy-tripdata.csv')
df11 = pd.read_csv('..\\Data\\raw\\Novembro-divvy-tripdata.csv')
df12 = pd.read_csv('..\\Data\\raw\\Dezembro-divvy-tripdata.csv')

# %%

juncao = pd.concat([df01, df02, df03, df04, df05, df06, df07, df08, df09, df10, df11, df12], ignore_index = True)


# %%

juncao.describe()
# %%

juncao = juncao.drop(columns=['start_lat', 'start_lng', 'end_lat', 'end_lng'], errors = 'ignore')

#%%

# Conhecendo o DataFrame 

print("\nLista de nomes da coluna:", juncao.columns)

print("\nTamanho do DataFrame: ", len(juncao))

print("\nDimensão do DataFrame: ", juncao.shape)

print("\nPrimeiras linhas do DataFrame: \n", juncao.head(6))

print("\nColunas e tipos de dados do DataFrame:")
juncao.info()

print("\nSumário das Estatísticas: ", juncao.describe())

#%%

# Modificação das colunas "started_at" e "ended_at" de object para datetime

juncao['started_at'] = pd.to_datetime(juncao['started_at'])
juncao['ended_at'] = pd.to_datetime(juncao['ended_at'])

#%%

# Adicionando colunas de data, mês, dia, ano e o dia da semana 
# Além disso, adicionando o calculo em segundos do tempo em que o cliente ficou com a Bicicleta

juncao['date'] = juncao['started_at'].dt.date
juncao['month'] = juncao['started_at'].dt.month
juncao['day'] = juncao['started_at'].dt.day
juncao['year'] = juncao['started_at'].dt.year
juncao['day_of_week'] = juncao['started_at'].dt.day_name()

juncao['ride_lenght'] = (juncao['ended_at'] - juncao['started_at']).dt.total_seconds()

#%%

# Verificou-se que existia valores negativos na medida ride_lenght
# Desse modo percemos que não teria como um cliente ficar tempo negativo em posse da blicicleta
# O cálculo abaixo faz a retirada destes dados negativos e salva em DF diferente

juncao_v2 = juncao[(juncao['start_station_name'] != "HQ QR") & (juncao['ride_lenght'] >= 0)].copy()


# %%

df_limpo = juncao_v2[juncao_v2['year'] != 2024]
df = df_limpo[df_limpo['ride_lenght'] <= 86400] 

df_limpo.head()
# %%

df.to_csv('..\Data\processed\Cleaned_Dataset.csv', index=False) 

# %%
