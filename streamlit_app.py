import streamlit as st

st.header('st.button')

if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

#nuova app

import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:')

# Example 2

st.write(1234)

# Example 3

df = pd.DataFrame({
     'first column': [1, 2, 3, 4],
     'second column': [10, 20, 30, 40]
     })
st.write(df)

# Example 4

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

# Example 5

df2 = pd.DataFrame(
     np.random.randn(200, 3), #genera una matrice 200x3 di numeri casuali distribuiti normalmente
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c) #crea un oggetto grafico basato sul dataframe. mark circle specifica che i punti siano cerchi, encode definisce come i dati saranno mappati. tooltip mostra i valori delle colonne quando ci si passa sopra il mouse

#######################  NUOVA APP SLIDER  ############

import streamlit as st
from datetime import time, datetime

st.header('st.slider')

# Example 1

st.subheader('Slider')

age = st.slider('How old are you?', 0, 130, 25)
st.write("I'm ", age, 'years old')

# Example 2

st.subheader('Range slider')

values = st.slider(
     'Select a range of values',
     0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

# Example 3 
    
# NB=Streamlit capisce automaticamente 
# che si tratta di uno slider con formato "oratio" 
# perché gli sto passando una tupla di oggetti 
# datetime.time come valore iniziale (value)


st.subheader('Range time slider')

appointment = st.slider(
     "Schedule your appointment:",
     value=(time(11, 30), time(12, 45)))
st.write("You're scheduled for:", appointment)

# Example 4

st.subheader('Datetime slider')

start_time = st.slider(
     "When do you start?",
     value=datetime(2020, 1, 1, 9, 30),
     format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)



########################### APP LINE CHART ##############

import streamlit as st
import pandas as pd
import numpy as np

st.header('Line chart')

chart_data = pd.DataFrame(
     np.random.randn(20, 3), #genera una matrice di numeri casuali, con 20 righe e 3 colonne
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


########################### APP SELECT BOX ##############

import streamlit as st

st.header('st.selectbox')

option = st.selectbox(
     'What is your favorite color?',
     ('Blue', 'Red', 'Green'))

st.write('Your favorite color is ', option)

########################### APP MULTISELECT ##############

import streamlit as st

st.header('st.multiselect')

options = st.multiselect(
     'What are your favorite colors',
     ['Green', 'Yellow', 'Red', 'Blue','Pink', 'Liliac'],
     ['Yellow', 'Red']) #opzioni default

st.write('You selected:', options)

########################### APP MULTISELECT ##############

import streamlit as st

st.header('st.checkbox')

st.write ('What would you like to order?')

icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
     st.write("Great! Here's some more 🍦")

if coffee: 
     st.write("Okay, here's some coffee ☕")

if cola:
     st.write("Here you go 🥤")

########## APP LATEX  ###################

import streamlit as st

st.header('st.latex')

st.latex(r'''
     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)
     ''') 
# r indica che la stringa à raw, quindi python non 
# deve interpretare eventuali caratteri speciali come 
# \n. Questo mi consente di scrivere in LaTex 
# ''' indica il multilinea, che permette di scrivere 
# stringhe su più righe (per formule lunghe o testi 
# formattati)


##################### CUSTOMIZZAZIONE APP ############

import streamlit as st

st.title('Customizing the theme of Streamlit apps')

st.write('Contents of the `.streamlit/config.toml` file of this app')

st.code("""
[theme]
primaryColor="#80DEEA"
backgroundColor="#E3F2FD"
secondaryBackgroundColor="#BA68C8"
textColor="#FFFFFF"
font="monospace"
""")

number = st.sidebar.slider('Select a number:', 0, 10, 5)
st.write('Selected number from slider widget is:', number)
