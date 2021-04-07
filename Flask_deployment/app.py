import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return 'Welcome everyone'
    
@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Health care provider fraud detection web app
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: num_procedure_code1
        in: query
        type: number
        required: true
      - name: num_procedure_code2
        in: query
        type: number
        required: true
      - name: num_procedure_code3
        in: query
        type: number
        required: true
      - name: num_admit_diagnosis_code
        in: query
        type: number
        required: true
      - name: num_diagnosis_code1
        in: query
        type: number
        required: true
      - name: num_diagnosis_code2
        in: query
        type: number
        required: true
      - name: num_diagnosis_code5
        in: query
        type: number
        required: true
      - name: num_diagnosis_code6
        in: query
        type: number
        required: true
      - name: num_diagnosis_code7
        in: query
        type: number
        required: true
      - name: num_diagnosis_code9
        in: query
        type: number
        required: true
      - name: num_diagnosis_code10
        in: query
        type: number
        required: true
      - name: num_attending_physician
        in: query
        type: number
        required: true
      - name: num_operating_physician
        in: query
        type: number
        required: true
      - name: num_other_physician
        in: query
        type: number
        required: true
      - name: num_Month_0
        in: query
        type: number
        required: true
      - name: num_race_2
        in: query
        type: number
        required: true
      - name: num_race_3
        in: query
        type: number
        required: true
      - name: num_race_5
        in: query
        type: number
        required: true
      - name: num_Renal_indicator
        in: query
        type: number
        required: true
      - name: Avg_reimbursement_amt
        in: query
        type: number
        required: true
      - name: Avg_age
        in: query
        type: number
        required: true
      - name: Avg_days_admit
        in: query
        type: number
        required: true
      - name: num_states_operate
        in: query
        type: number
        required: true
      - name: num_counties
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    num_procedure_code1=request.args.get("num_procedure_code1")
    num_procedure_code2=request.args.get("num_procedure_code2")
    num_procedure_code3=request.args.get("num_procedure_code3")
    num_admit_diagnosis_code=request.args.get("num_admit_diagnosis_code")
    num_diagnosis_code1=request.args.get("num_diagnosis_code1")
    num_diagnosis_code2=request.args.get("num_diagnosis_code2")
    num_diagnosis_code5=request.args.get("num_diagnosis_code5")
    num_diagnosis_code6=request.args.get("num_diagnosis_code6")
    num_diagnosis_code7=request.args.get("num_diagnosis_code7")
    num_diagnosis_code9=request.args.get("num_diagnosis_code9")
    num_diagnosis_code10=request.args.get("num_diagnosis_code10")
    num_attending_physician=request.args.get("num_attending_physician")
    num_operating_physician=request.args.get("num_operating_physician")
    num_other_physician=request.args.get("num_other_physician")
    num_Month_0=request.args.get("num_Month_0")
    num_race_2=request.args.get("num_race_2")
    num_race_3=request.args.get("num_race_3")
    num_race_5=request.args.get("num_race_5")
    num_Renal_indicator=request.args.get("num_Renal_indicator")
    Avg_reimbursement_amt=request.args.get("Avg_reimbursement_amt")
    Avg_age=request.args.get("Avg_age")
    num_states_operate=request.args.get("num_states_operate")
    Avg_days_admit=request.args.get("Avg_days_admit")
    num_counties=request.args.get("num_counties")
    prediction=model.predict([[num_procedure_code1,num_procedure_code2,num_procedure_code3,
    					num_admit_diagnosis_code,num_diagnosis_code1,num_diagnosis_code2,num_diagnosis_code5,
    					num_diagnosis_code6,num_diagnosis_code7,num_diagnosis_code9,num_diagnosis_code10,
    					num_attending_physician,num_operating_physician,num_other_physician,num_Month_0,
    					num_race_2,num_race_3,num_race_5,num_Renal_indicator,
    					Avg_reimbursement_amt,Avg_reimbursement_amt,Avg_age,num_states_operate,Avg_days_admit,num_counties]])
    					
    if prediction==1:
    	return 'Beware.This provider looks fraudulent'
    else:
    	return 'No need to worry. This provider is not fraudulent'

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if output==1:
    	return render_template('index.html', prediction_text='Beware.This provider looks fraudulent')
    else:
    	return render_template('index.html', prediction_text='No need to worry. This provider is not fraudulent')	

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config.PORT, debug=config.DEBUG_MODE)
