#%%

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%

df = pd.read_csv('..\\Data\\processed\\Cleaned_Dataset.csv', low_memory = False)


#%%
#Realizando Análise Descritiva

print("Realizando Análise Descritiva da coluna ride_lenght: \n", df['ride_lenght'].describe())
# %%

# Comparação de usuário membros e casual 

print("\nEstatística de duração da viagem agrupado por membro_casual: \n")
df.groupby('member_casual')['ride_lenght'].agg(['mean', 'median', 'max', 'min'])
# %%

# Realizando a média para saber quais os dias que cada grupo de usuário mais utiliza
# o serviço de bicicleta 

print("\nMédia de duração de viagem por tipo de membro e dia da semana: \n\n",
        df.groupby(['member_casual', 'day_of_week'])['ride_lenght'].mean())
# %%

# Ordenando os dias da semana

days_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

df['day_of_week']= pd.Categorical(df['day_of_week'], categories = days_order, ordered = True)

# %%

print("\nMédia de duração de viagem por tipo de membro e dia da semana: \n\n",
        df.groupby(['member_casual', 'day_of_week'])['ride_lenght'].mean())

# %%

summary_stats = df.groupby(['member_casual', 'day_of_week']).agg(
    number_of_rides = ('ride_id', 'count'),
    average_duration = ('ride_lenght', 'mean'),
).reset_index()

print("\nResumo das viagens e duração por tipo de passageiros e dia da semana.\n\n", summary_stats)
# %%

# %%
counts = df.groupby(['member_casual',
'day_of_week'])['ride_lenght'].mean().reset_index()
counts.to_csv('avg_ride_length.csv', index=False)
# %%

# Gráfico da média geral de tempo utilizado durante a semana.

counts = df.groupby(['member_casual', 'day_of_week'])['ride_lenght'].mean().reset_index()

sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))


sns.barplot(
    data=counts, 
    x='day_of_week', 
    y='ride_lenght', 
    hue='member_casual'
)


plt.title('Média de Duração da Viagem por Dia da Semana', fontsize=14)
plt.xlabel('Dia da Semana', fontsize=12)
plt.ylabel('Média de Duração (segundos/minutos)', fontsize=12)
plt.legend(title='Tipo de Membro')

plt.show()
# %%

# Gráfico para saber a média anual de tempo em Segundos de utilização 
# e o crescimento do ano de 2019 para o de 2020 no primeiro Trimestre do Ano durante a semana.

counts = df.groupby(['year','member_casual', 'day_of_week'])['ride_lenght'].mean().reset_index()


g = sns.catplot(
    data=counts, 
    kind="bar",
    x="day_of_week", 
    y="ride_lenght", 
    hue="member_casual",
    col="year",        
    col_wrap=2,        
    height=5, 
    aspect=1.2
)


g.set_axis_labels("Dia da Semana", "Média de Duração")
g.set_titles("Ano: {col_name}")
g._legend.set_title("Tipo de Usuário")

plt.show()
