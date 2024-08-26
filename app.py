import streamlit as st # Desenvolvimento web
import numpy as np  
import pandas as pd 
import time  
import plotly.express as px # interação

# csv
df = pd.read_csv("bank.csv", sep=',')

st.set_page_config(
    page_title = 'Painel em tempo real',
    page_icon = '✅',
    layout = 'wide'
)

# Título do dashboard
st.title("Ao vivo / Dashboard")

# Filtros
job_filter = st.selectbox("Selecione a profissão", pd.unique(df['profissao']))

# Criando um container
placeholder = st.empty()

# filtrar  
df = df[df['profissao']==job_filter]

# Simulação "ao vivo"
for seconds in range(200):
    df['age_new'] = df['idade'] * np.random.choice(range(1,5))
    df['balance_new'] = df['renda'] * np.random.choice(range(1,5))

    # Criando KPI  
    avg_age = np.mean(df['age_new']) 

    count_married = int(df[(df["estadoCivil"]=='casado')]['estadoCivil'].count() + np.random.choice(range(1,30)))
    
    balance = np.mean(df['balance_new'])

    with placeholder.container():
        # criando três colunas no Dashboard
        kpi1, kpi2, kpi3 = st.columns(3)

        # Preenchendo as três colunas 
        kpi1.metric(label="Idade ⏳", value=round(avg_age), delta= round(avg_age) - 10)
        kpi2.metric(label="Contando casamento 💍", value= int(count_married), delta= - 10 + count_married)
        kpi3.metric(label="Renda ＄", value= f"$ {round(balance,2)} ", delta= - round(balance/count_married) * 100)

        # Criar duas colunas
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Primeiro gráfico")
            fig = px.density_heatmap(data_frame=df, y = 'age_new', x = 'estadoCivil')
            st.write(fig)
        with fig_col2:
            st.markdown("### Segundo gráfico")
            fig2 = px.histogram(data_frame = df, x = 'age_new')
            st.write(fig2)
        st.markdown("### Visualização detalhada")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()


