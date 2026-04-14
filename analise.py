#%% Importando os pacotes necessários
import pandas as pd
import prince
import matplotlib.pyplot as plt

#%% Carregando os dados
caminho = 'dados_consultoria_juridica.csv'
df = pd.read_csv(caminho)


#%% Criar a tabela de contingência (Setor vs Desfecho)
contingency_table = pd.crosstab(df['Setor'], df['Desfecho'])

#%% Inicializar e ajustar o modelo de CA
ca = prince.CA(n_components=2)
ca = ca.fit(contingency_table)

#%% Geração de graficos
ax = ca.plot_coordinates(
    X=contingency_table,
    ax=None,
    figsize=(8, 8),
    x_component=0,
    y_component=1,
    show_row_labels=True,
    show_col_labels=True
)
plt.title("Mapa Perceptual: Setor vs Desfecho")
plt.show()
