# import the required libraries

import numpy as np
import pandas as pd
import pickle
import streamlit as st


# provide header name to browser
st.set_page_config(page_title = 'cars93 Project Lokesh' , layout =  'wide')

# Add a title in body of browser
st.title('Cars93 Project by Lokesh Chakranarayan ')

EngineSize = st.number_input('EngineSize: ', min_value = 0.00, step=0.01)
Horsepower = st.number_input('Horsepower : ', min_value = 0.00, step=0.01)
MPG.city = st.number_input('MPG.city : ', min_value = 0.00, step=0.01)
MPG.highway = st.number_input('MPG.highway: ', min_value = 0.00, step=0.01)