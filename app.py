import streamlit as st
import numpy as np 
import pandas as pd 
import pickle  

with open('model_pickle','rb') as model:
    model_rfc = pickle.load(model)

def main():
    html_temp = """ <div style = "background-color :pink;padding:10px">
    <h1 style = "color:white;text-align:center">Diabetes Prediction</h2>
    </div>

    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.markdown('_Markdown_')

    

       





if __name__ == '__main__':
    main()


#print(model_rfc.predict([[40,0,1,1,0,0,0,1,1,1]]))
