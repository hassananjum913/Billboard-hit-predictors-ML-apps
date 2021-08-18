# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 02:03:16 2021

@author: Anjum
"""


import streamlit as st
from PIL import Image
import pickle


model = pickle.load(open('./Model/ML_Model1.pkl', 'rb'))

def run():
    
    img1 = Image.open('billboard_hit.jpg')
    img1 = img1.resize((200,145))
    st.image(img1,use_column_width=False)
    st.title("BillBoard Hit Prediction using Machine Learning")
    

   
    instrumentalness = st.number_input('Enter instrumentalness value: Ex:0.000045') 
    st.markdown( "{:.6f}".format(instrumentalness) )
        
    acousticness = st.number_input('Enter acousticness value: Ex:0.016400')
    st.markdown("{:.6f}".format(acousticness))
    
    loudness = st.number_input('Enter loudness value: Ex:-7.776')
    st.markdown("{:.4f}".format(loudness))
        
    energy = st.number_input('Enter energy value: Ex:0.7865')
    st.markdown("{:.4f}".format(energy))
        
    duration_ms = st.number_input('Enter duration in ms value: Ex:673445')
    st.markdown("{:.1f}".format(duration_ms))
    
    valence = st.number_input('Enter valence value: Ex:0.4569')
    st.markdown("{:.4f}".format(valence))
        
    danceability = st.number_input('Enter danceability value: Ex:0.658')
    st.markdown("{:.3f}".format(danceability))
    
        
    liveness = st.number_input('Enter liveness value: Ex:0.2387')
    st.markdown("{:.4f}".format(liveness))
    
  
        
        
    if st.button("Submit"):
        
        features= [[instrumentalness,acousticness,loudness,energy,duration_ms,valence,danceability,liveness]]
        
        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))
        if ans == 0:
            st.error("It's not a Hit")
        else:
            st.success("It's a Hit")

run()