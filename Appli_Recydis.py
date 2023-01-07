iimport streamlit as st
import pandas as pd
import numpy as np
import pickle
from PIL import Image
#import matplotlib
#import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import json
import plotly.express as px
import altair as alt



def identifiant_comm():
        ID_comm=st.sidebar.selectbox('Commercial(e)',(X[['Commercial(e)']]))

        data={' ID_comm ': ID_comm }
    
        ID_client = pd.DataFrame(data,index=[0])
        return ID_client


if __name__=="__main__":
    st.set_page_config(
        page_title="Streamlit basics app",
        layout="centered"
    )

    st.title("Analyses pour déterminer la fillière de traitement adéquate")

    st.write("Auteur : Brahim AIT OUALI  - Data Scientist")
  

    # Display the LOGO
    img = Image.open("LOGO_RECYDIS.png")
    st.sidebar.image(img, width=300)

    #Collecter le profil d'entrée
    st.sidebar.header("Identifiant du client")




    X = pd.read_excel( 'Tableau_Recydis.xlsx')
    X=pd.DataFrame(X)



    input_df=identifiant_comm().iloc[0,0]



    donnees_comm = X[X['Commercial(e)']==input_df] # ligne du dataset qui concerne le client
    st.write(donnees_comm)
        
    st.write("Calendrier d'étalonnage du PH-mètre")
    
    y = pd.read_excel( 'Etalonnage Ph-mètre.xlsx')
    y=pd.DataFrame(y)
    st.write(y)
    



