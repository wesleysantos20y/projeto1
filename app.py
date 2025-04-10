import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("projeto1")
st.divider()

diamentro = st.number_input("digite o tamanho do diamentro da pizza: ")

if diamentro:
    preco_previsto = modelo.predict([[diamentro]])[0][0]
    st.write(f"o valor da pizza com diamentro de {diamentro} e de R${preco_previsto}.")