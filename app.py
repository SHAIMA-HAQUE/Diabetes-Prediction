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
    st.markdown('### Age')
    age = st.slider('Slide me',min_value = 0,max_value = None)

    st.markdown("### Polyuria")
    polyuria = st.radio('Choose', ['Yes','No'])
    if polyuria == 'Yes':
        polyuria = 1
    elif polyuria == 'No':
        polyuria = 0
    
    st.markdown("### Polydipsia")
    polydipsia = st.radio('Choose the correct option',['Yes','No'])
    if polydipsia == 'Yes':
        polydipsia = 1
    elif polydipsia == 'No':
        polydipsia = 0
    
    st.markdown('### Gender')
    gender = st.radio('Select the suitable option', ['Male','Female'])
    if gender == 'Male':
        gender = 1
    elif gender == 'Female':
        gender = 0
    
    st.markdown('### Partial Paresis')
    partial_paresis = st.radio('Select',["Yes","No"])
    if partial_paresis == 'Yes':
        partial_paresis = 1
    elif partial_paresis == 'No':
        partial_paresis = 0
    
    st.markdown('### Sudden Weight Loss')
    weight_loss = st.radio('Select the option bases on your observation',["Yes","No"])
    if weight_loss == 'Yes':
        weight_loss = 1
    elif weight_loss == 'No':
        weight_loss = 0
    
    st.markdown('### Irritability')
    irritability = st.radio('Select based on what you are feeling recently',["Yes","No"])
    if irritability == 'Yes':
        irritability = 1
    elif irritability == 'No':
        irritability = 0
    
    st.markdown('### Delayed healing')
    healing = st.radio('Select yes if wounds take time to heal',["Yes","No"])
    if healing == 'Yes':
        healing = 1
    elif healing == 'No':
        healing = 0
    
    st.markdown('### Alopecia')
    alopecia = st.radio('Select yes if symptoms are present',["Yes","No"])
    if alopecia == 'Yes':
        alopecia = 1
    elif alopecia == 'No':
        alopecia = 0
    
    st.markdown('### Itching')
    itching = st.radio('Select yes if constantly occuring',["Yes","No"])
    if itching == 'Yes':
        itching = 1
    elif itching == 'No':
        itching = 0
    
    if st.button('Predict'):
        result = prediction(age,polyuria,polydipsia,gender,partial_paresis,weight_loss,irritability,healing,alopecia,itching)
        if result == 1:
            st.error('Chance of diabetes. Do not panic. Consult a doctor')
        elif result == 0:
            st.success('Diabetes not predicted')


    st.sidebar.header("Some Important Terms: ")
    # st.sidebar.markdown("
    # [Polyuria]()

    # ")

def prediction(age,polyuria,polydipsia,gender,partial_paresis,weight_loss,irritability,healing,alopecia,itching):
    predicted_output = model_rfc.predict([[age,polyuria,polydipsia,gender,partial_paresis,weight_loss,irritability,healing,alopecia,itching]])
    return predicted_output

if __name__ == '__main__':
    main()
#print(model_rfc.predict([[40,0,1,1,0,0,0,1,1,1]]))
