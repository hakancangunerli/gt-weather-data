# %%
#https://cdn.weatherstem.com/dashboard/data/dynamic/model/gatech/stadium/latest.json

import pandas as pd
import requests
import json
import streamlit as st
import numpy as np
st.title("Georgia Tech Weather \"App\"")
st.write("This is a weather app using data from Georgia Tech Weather Station")

address = "https://cdn.weatherstem.com/dashboard/data/dynamic/model/gatech/stadium/latest.json"

def get_data(address):
    r = requests.get(address)
    data = r.json()
    return data

# export this json file
with open('gt.json', 'w') as f:
    json.dump(get_data(address), f)

df = pd.DataFrame(get_data(address))

df.drop('validation_sensor', axis=1, inplace=True)

# %%
# we have three cameras in the stadium, gatechsw, gatecheast, and cumulus
# https://gatech.weatherstem.com/skycamera/gatech/stadium/cumulus/snapshot.jpg
# https://gatech.weatherstem.com/skycamera/gatech/stadium/gatecheast/snapshot.jpg

cameras = ['gatechsw', 'gatecheast', 'cumulus']

pictures = []

for camera in cameras:
    pictures.append(f"https://gatech.weatherstem.com/skycamera/gatech/stadium/{camera}/snapshot.jpg")

# show the pictures side by side

st.write("Data from Georgia Tech Weather Station:")
# ignore bool warning from numpy 
with np.errstate(invalid='ignore'):
    st.write(df)



# print temperature which is at index 14
st.write("Temperature in Fahrenheit is:", df['records'][14]['value'])

# print wind speed 
st.write("Wind Speed in MPH is:", df['records'][4]['value'])

#rainfall is at index 11 
st.write("Rainfall in Inches is:", df['records'][11]['value'])

# show images 
st.write("Images from Georgia Tech Weather Station:")
st.image(pictures, width=500)