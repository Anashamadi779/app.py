import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

st.title("La Statistique Descriptive")

uploaded_file = st.file_uploader("Choisissez un fichier Excel ou CSV", type=["xlsx", "csv"])

if uploaded_file:
    
    if uploaded_file.name.endswith('csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    st.write("Aperçu des données :")
    st.dataframe(df, use_container_width=True)

    column = st.selectbox("Sélectionnez une colonne pour visualiser :", df.columns)

    fonction = st.selectbox("Choisissez la fonction de statistique descriptive :", 
                                  ["Moyenne", "Médiane", "Écart-type", "Variance", "Minimum", "Maximum", "Q1", "Q3", "IQR"])

    if fonction == "Moyenne":
        result = round(np.mean(df[column]),2)
    elif fonction == "Médiane":
        result = round(np.median(df[column]),2)
    elif fonction == "Écart-type":
        result = round(np.std(df[column], ddof = 1),2)
    elif fonction == "Variance":
        result = round(np.var(df[column], ddof = 1),2)
    elif fonction == "Minimum":
        result = round(np.min(df[column]),2)
    elif fonction == "Maximum":
        result = round(np.max(df[column]),2)
    elif fonction == "Q1":
        result = round(np.percentile(df[column], 25),2)
    elif fonction == "Q3":
        result = round(np.percentile(df[column], 75),2)
    elif fonction == "IQR":
        result = round(np.percentile(df[column], 75) - np.percentile(df[column], 25),2)

    st.write(str(fonction) + "de " + str(column) + "est : " + str(result))

    graphe = st.selectbox("Choisissez le type de graphique :", ["Histogramme","Barres", "Boîte à moustaches"])

    labels = ['Moyenne', 'Médiane', 'Variance', 'Écart-type','max','min']
    values = [np.mean(df[column]), np.median(df[column]), np.var(df[column]), np.std(df[column], ddof = 1),np.max(df[column]),np.min(df[column])]

    if graphe == "Histogramme":
        st.subheader("Histogramme")
        plt.figure(figsize=(10, 5))
        sns.histplot(df[column], bins=30)
        plt.title("Histogramme de " + str(column))
        plt.ylabel("Valeurs")
        st.pyplot(plt)  

    elif graphe == "Barres":
        st.subheader("Barres")
        plt.figure(figsize=(10,5))
        plt.bar(labels, values, color=['blue', 'green', 'red', 'purple','yellow','orange'])
        plt.ylabel("Valeurs")
        plt.yscale('log')
        plt.title("Barres de " + str(column))
        st.pyplot(plt)
       
    elif graphe == "Boîte à moustaches":
        st.subheader("Boîte à moustaches")
        plt.figure(figsize=(10,5))
        sns.boxplot(x=df[column], showmeans=True, meanline=True, 
                         medianprops={'color': 'red', 'linewidth': 2}, 
                         capprops={'color': 'blue', 'linewidth': 2}, 
                         boxprops={'color': 'yellow', 'linewidth': 2})
        plt.title("Boîte à moustaches de " + str(column))
        st.pyplot(plt)
