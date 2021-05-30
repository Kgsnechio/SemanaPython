import pandas as pd 
import plotly.express as px

tabelaClientes = pd.read_csv("telecom_users.csv")

tabelaClientes = tabelaClientes.drop('Unnamed: 0', axis=1)
tabelaClientes = tabelaClientes.drop('IDCliente', axis=1)

tabelaClientes['TotalGasto'] = pd.to_numeric(tabelaClientes['TotalGasto'], errors='coerce')

tabelaClientes = tabelaClientes.dropna(how='all', axis=1)
tabelaClientes = tabelaClientes.dropna()

status = tabelaClientes['Churn'].value_counts(normalize= True)

pizza = px.pie(tabelaClientes, 'Churn').update_traces(textinfo="label+value+percent")
pizza.show()

for tabela in tabelaClientes:
    grafico = px.histogram(tabelaClientes, x=tabela, color='Churn', barnorm='percent')
    grafico.show()