import streamlit as st
import pandas  #Lê os csv

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Luís Silva")
    content="""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    """
    st.info(content)

content2="""
Abaixo podes ver e fazer muitas coisas construidas em python. Contacta-me
"""
st.write(content2)



col3,col4 = st.columns(2)

df=pandas.read_csv("data.csv",sep=";") #abre o ficheiro w atribui-o a uma data frame

print(df)

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])