import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('model.pkl', 'rb'))

def main():
    st.title('Healthcare provider fraud detector')
    html_temp="""
    <div style="background-color:teal;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Healthcare provider fraud detector app </h2>
   """ 
    st.markdown(html_temp,unsafe_allow_html=True)
    num_procedure_code1=st.text_input("num_procedure_code1",0)
    num_procedure_code2=st.text_input("num_procedure_code2",0)
    num_procedure_code3=st.text_input("num_procedure_code3",0)
    num_admit_diagnosis_code=st.text_input("num_admit_diagnosis_code",0)
    num_diagnosis_code1=st.text_input("num_diagnosis_code1",0)
    num_diagnosis_code2=st.text_input("num_diagnosis_code2",0)
    num_diagnosis_code5=st.text_input("num_diagnosis_code5",0)
    num_diagnosis_code6=st.text_input("num_diagnosis_code6",0)
    num_diagnosis_code7=st.text_input("num_diagnosis_code7",0)
    num_diagnosis_code9=st.text_input("num_diagnosis_code9",0)
    num_diagnosis_code10=st.text_input("num_diagnosis_code10",0)
    num_attending_physician=st.text_input("num_attending_physician",0)
    num_operating_physician=st.text_input("num_operating_physician",0)
    num_other_physician=st.text_input("num_other_physician",0)
    num_Month_0=st.text_input("num_Month_0",0)
    num_race_2=st.text_input("num_race_2",0)
    num_race_3=st.text_input("num_race_3",0)
    num_race_5=st.text_input("num_race_5",0)
    num_Renal_indicator=st.text_input("num_Renal_indicator",0)
    Avg_reimbursement_amt=st.text_input("Avg_reimbursement_amt",0)
    Avg_age=st.text_input("Avg_age",0)
    num_states_operate=st.text_input("num_states_operate",0)
    Avg_days_admit=st.text_input("Avg_days_admit",0)
    num_counties=st.text_input("num_counties",0)
    if st.button('Predict'):
        prediction=model.predict([[num_procedure_code1,num_procedure_code2,num_procedure_code3,
     					num_admit_diagnosis_code,num_diagnosis_code1,num_diagnosis_code2,num_diagnosis_code5,
     					num_diagnosis_code6,num_diagnosis_code7,num_diagnosis_code9,num_diagnosis_code10,
     					num_attending_physician,num_operating_physician,num_other_physician,num_Month_0,
     					num_race_2,num_race_3,num_race_5,num_Renal_indicator,
     					Avg_reimbursement_amt,Avg_reimbursement_amt,Avg_age,num_states_operate,Avg_days_admit,num_counties]])
        if prediction==0:
            st.success('This provider doesn\'t seem to be fraudulent')
        else:
            st.success('Beware! This provider seems fraudulent')

if __name__ == "__main__":
    main()
