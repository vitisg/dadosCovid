import pandas as pd
import plotly.express as px
import streamlit as st

#importando os dados do repositorio do github de Wesley Cota
df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

#renomeando as colunas para melhorar na visualização
df = df.rename(columns={'newDeaths': 'Novas mortes', 'newCases': 'Novos casos', 'totalCases': 'Total de casos', 'deaths_per_100k_inhabitants': 'Mortes por 100 mil habitantes' })

#atribuindo a barra de seleção para o estado
estados = list(df['state'].unique())
state = st.sidebar.selectbox('Qual o estado?', estados)
#sidebar vai colocar barra lateral no site, selectbox vai colocar uma barra de seleção que vai ficar no sidebar

#atribuindo a barra de seleção para o tipo de informação
colunas = ['Novas mortes','Novos casos','Total de casos', 'Mortes por 100 mil habitantes' ]
column = st.sidebar.selectbox('Qual tipo de informação?', colunas)

#definindo o estado
df = df[df['state'] == state]

#criando os textos e o gráfico
st.title('DADOS COVID - BRASIL')
st.write('Nessa aplicação, o usuário tem a opção de escolher o estado e o tipo de informação para mostrar o grafico. Utilize o menu lateral para alterar a amostragem')
fig = px.line(df, x="date", y=column, title=column + ' - ' + state)
fig.update_layout(xaxis_title="Data", yaxis_title=column.upper(), title={'x': 0.5})
st.plotly_chart(fig, use_container_width=True)
st.caption('Os dados foram obtidos a partir o site: https://github.com/wcota/covid19br')


with st.expander("See explanation"):
    st.write("Os dados apresentados são sempre atualizados de acordo com o decorrer das informações" )
