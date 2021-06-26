import streamlit as st
import numpy as np 
import pandas as pd 
import pickle  

with open('model_pickle','rb') as model:
    model_rfc = pickle.load(model)

def main():
    html_temp = """ <div style = "background-color :pink;padding:10px">
    <h1 style = "color:white;text-align:center">Diabetes Predictor</h2>
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
    st.sidebar.write("""
     _Click on the terms to know what they mean_
    - **[POLYURIA](https://www.webmd.com/diabetes/polyuria-too-much-urine#:~:text=If%20you%20have%20a%20condition,a%20classic%20sign%20of%20diabetes.)** 

    - **[POLYDIPSIA](https://www.healthline.com/health/diabetes/polydipsia#:~:text=Polydipsia%20is%20a%20medical%20name,lose%20a%20lot%20of%20fluid.)**

    - **[PARTIAL PARESIS](https://www.healthline.com/health/paresis#:~:text=Paresis%20involves%20the%20weakening%20of,occurs%20when%20nerves%20are%20damaged.)**

    - **[ALOPECIA](https://www.healthline.com/health/alopecia-areata#:~:text=Alopecia%20areata%20is%20a%20condition,follicles%2C%20resulting%20in%20hair%20loss.)**

    - **[SUDDEN WEIGHTLOSS](https://my.clevelandclinic.org/health/diseases/17770-unexplained-weight-loss)**
        - Weight loss of 10 pounds or more, or five percent of body weight, over a period of 6 to 12 months is considered “unexplained.”
    """)
     
    if st.button("Remedies"):
        if polyuria == 1:
            st.write("""
            ** For Polyuria:**
            - Consult a doctor
            - Cut Back on alcohol and caffeine
             """)
        if polydipsia == 1:
            st.write("""
            ** For Polydipsia:**
            - Consult a doctor
            - Form a exercise plan and stick to it
            - Try to take less stress
             """)
        if partial_paresis == 1:
            st.write("""
            ** For Partial Paresis: **
            - Do not panic, consult a doctor
             """)
        if alopecia == 1:
            st.write(""" 
            ** For Alopecia:**
            - Manage your stress levels by taking a walk everyday.
            - Consult your doctor
            - Check twice before taking any medication
            """)

def prediction(age,polyuria,polydipsia,gender,partial_paresis,weight_loss,irritability,healing,alopecia,itching):
    predicted_output = model_rfc.predict([[age,polyuria,polydipsia,gender,partial_paresis,weight_loss,irritability,healing,alopecia,itching]])
    return predicted_output

if __name__ == '__main__':
    main()

