# código de geração do gráfico 
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('gasolina.csv', sep=',')

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço Médio Venda Gasolina em SP', xlabel='Dia', ylabel='Preço');

plt.savefig('gasolina.png')

print('Sucesso')