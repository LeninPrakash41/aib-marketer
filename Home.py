import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Marketer - No Code Marketing Analysitcs", 
                page_icon=":robot_face:",
                layout="wide",
                initial_sidebar_state="expanded"
                )
from re import X


#########
#SIDEBAR
########

st.title('</>AI Marketer - No Code Marketing Analytics by AI')
st.subheader('Analyze your marketing data by AI & ML algorithms without a single-line of code.')
st.write('With our cutting-edge AI, we give you answer in numbers, text, tables, and charts.')
st.write('You can use AI to handle your marketing task now !')

st.text('')

st.image('modules1.png')
st.image('modules2.png')


st.text('')
