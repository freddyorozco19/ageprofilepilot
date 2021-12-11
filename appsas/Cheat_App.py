# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 07:26:47 2021

@author: fredd
"""

"""
Streamlit Cheat Sheet
App to summarise streamlit docs v0.81.0 for quick reference
There is also an accompanying png version
https://github.com/daniellewisDL/streamlit-cheat-sheet
v0.71.0 November 2020 Daniel Lewis and Austin Chen
"""
import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib as mpl
from pathlib import Path
import base64
from hydralit import HydraHeadApp
import os
from matplotlib import font_manager as fm, rcParams
import matplotlib.patheffects as path_effects



# Thanks to streamlitopedia for the following code snippet
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


class CheatApp(HydraHeadApp):

    def __init__(self, title = '', **kwargs):
        self.__dict__.update(kwargs)
        self.title = title
        
    def run(self):

        self._cs_sidebar()
        self._cs_body()


    # sidebar

    def _cs_sidebar(self):

        st.sidebar.header('Streamlit cheat sheet')

      
        return None

    ##########################
    # Main body of cheat sheet
    ##########################

    def _cs_body(self):
        # Magic commands
        
        fpath2 = os.path.join(mpl.get_data_path(), "resources/keymer-bold.otf")
        prop2 = fm.FontProperties(fname=fpath2)
        fname2 = os.path.split(fpath2)[1]

        df = pd.read_csv('LIGACOL21FULL_25112021_TxT_LBP2_ADV_SEARCH.csv', sep = ';')

        df['90s'] = df['Minutes played']/90

        #calc_elements = ['goals', 'assists', 'points']

        #for each in calc_elements:
            #    df[f'{each}_p90'] = df[each] / df['90s']

        positions = list(df['Position'].drop_duplicates())
        teams = list(df['Team'].drop_duplicates())
        ages = list(df['Age'].drop_duplicates())

        position_choice = st.sidebar.multiselect(
            'Choose position:', positions, default=positions)
        teams_choice = st.sidebar.multiselect(
            "Teams:", teams, default=teams)
        ages_choice = st.sidebar.multiselect(
            'Choose age:', ages, default = ages)
        price_choice = st.sidebar.slider(
            'Max Price:', min_value=4.0, max_value=15.0, step=.5, value=15.0)
        
        
        df = df[df['Position'].isin(position_choice)]
        df = df[df['Team'].isin(teams_choice)]
        df = df[df['Age'].isin(ages_choice)]

        # Main
        st.title(f"PRIMERA DIVISIÓN DE COLOMBIA")
        

        fig, ax = plt.subplots(figsize = (8, 6), dpi = 800)
        fig.set_facecolor('#061123')
        ax.patch.set_facecolor('#061123')
        mpl.rcParams['xtick.color'] = 'white'
        mpl.rcParams['ytick.color'] = 'white'
        
        #agesrange = st.multiselect('Define el rango de edad', ages, default = ages)
        #aage = st.slider("Label", 16, 42, (20, 30), 1)
        aage = st.slider(
        'SELECCIONA EL RANGO DE EDAD',
        16, 42, (20, 25))
        #st.write('Values:', type(aage))
        
        #aage = st.slider('Define el rango de edad', min_value=16, max_value=42, (20,30), step = 1)
        df = df[df['Age'] <= max(aage)]
        df = df[df['Age'] > min(aage)]

#        track = fig.text(0.22,1.05,'DEPORTIVO CALI', fontproperties=prop2, fontsize=22, color="#00A78D")

        xcol = df['Age']
        ycol = df['90s']
        plt.scatter(xcol, ycol, color = "#FF0046", edgecolors = "#FFF", alpha = 0.5)
        pes = plt.xlabel('EDAD', fontsize=13, color="w", labelpad=20)
        pes.set_path_effects([path_effects.withStroke(linewidth=3, foreground="#000")])
        pas = plt.ylabel('NÚMERO DE 90 MINUTOS JUGADOS', fontsize=12, color="w", labelpad=20)
        pas.set_path_effects([path_effects.withStroke(linewidth=3, foreground="#000")])

        #Spines
        spines =["top", "right", "bottom", "left"]
        for s in spines:
            ax.spines[s].set_color("w")
        
        st.pyplot(fig)

        return None