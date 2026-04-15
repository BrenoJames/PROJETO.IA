import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

# Função que cria o "cérebro" da IA
def treinar_modelo():
    dados = {
        'diametro': [30, 31, 32, 33, 34, 36, 37, 38, 39, 40, 41, 42],
        'preco': [23, 25, 27, 29, 31, 33, 36, 39, 41, 44, 46, 50]
    }
    df = pd.DataFrame(dados)
    modelo = LinearRegression()
    modelo.fit(df[['diametro']], df['preco'])
    return modelo

# Código da Interface
st.title("🍕 Medidor de Preço de Pizza")
modelo_treinado = treinar_modelo()

tamanho = st.number_input("Digite o diâmetro (cm):", min_value=10, max_value=60, value=35)

if st.button("Calcular Preço"):
    preco = modelo_treinado.predict([[tamanho]])
    st.success(f"O preço estimado é R$ {preco[0]:.2f}")
    st.balloons()