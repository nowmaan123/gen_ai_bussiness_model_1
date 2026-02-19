import streamlit as st

st.title('Content Generator')
prompt = st.text_area('Prompt')
if st.button('Generate'):
    st.write('Generated content placeholder for:', prompt)
