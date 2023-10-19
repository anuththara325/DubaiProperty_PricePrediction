import numpy as np
from flask import Flask, request, render_template, redirect, url_for, session
import pickle

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'q1w2e3r4t5y6'
       
model = pickle.load(open('Frontend/Model/model.pkl', 'rb'))
rfmodel = pickle.load(open('Frontend/Model/rfmodel.pkl', 'rb'))
     
prediction_labels = {
    1.0: "Low",  
    2.0: "Medium",
    3.0: "High", 
    4.0: "Ultra High"         
}       
 
radio_button_display_names = {
    0: "No",
    1: "Yes"
}

@app.route('/classification')
def classify(): 
    return render_template('classification.html')
 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/regression')
def rfression():
    return render_template('regression.html')       

@app.route('/predict', methods=['POST'])
def predict():   
    # Extract the input values from the form     
    input_values = {key: int(value) for key, value in request.form.items()}

    # Call your model's predict function with the input features
    prediction = model.predict([np.array(list(input_values.values()))])
    output = round(prediction[0], 2)
    output = float(output)     

    converted_values = {}

    # Create a dictionary to map radio button values to display names

    # Define the radio button field names
    radio_button_fields = ["Maid Room","Unfurnished","Balcony","Barbecue Area","Built in Wardrobes",
    "Central A/C","Childrens Play Area","Childrens Pool","Concierge","Covered Parking",
    "Kitchen Appliances", "Lobby in Building","Maid Service","Networked","Pets Allowed","Private Garden",
    "Private Gym","Private Jacuzzi","Private Pool","Security","Shared Gym","Shared Pool","Shared Spa",
    "Study","Vastu Compliant","View of Landmark","View of Water","Walk in Closet"]  

    # Iterate through the form values
    for field, value in input_values.items():
     if field in radio_button_fields:
        # Check if the value is in the mapping dictionary
        if value in radio_button_display_names:
            display_name = radio_button_display_names[value]
        else:
            # If not found in the mapping, keep the original value
            display_name = value
        converted_values[field] = display_name
     else:
        converted_values[field] = value
        
    #print(converted_values) 
       
    # Map the numerical prediction to a label
    if output in prediction_labels:
        decoded_prediction = prediction_labels[output]   
    else:
        decoded_prediction = "Unknown"  

    # Store the input values and prediction in session variables
    session['input_values'] = input_values
    session['converted_values']=converted_values
    session['prediction'] = decoded_prediction  # Store the decoded prediction label
 

    # Redirect to the result page
    return redirect(url_for('show_result'))

@app.route('/result')      
def show_result():
    # Retrieve the input values and decoded prediction from the session
    input_values = session.get('input_values', {})
    decoded_prediction = session.get('prediction', "Unknown")
    converted_values = session.get('converted_values',{})


    # Pass the input values and decoded prediction to the result.html template
    return render_template('resultclass.html', input_values=input_values, converted_values=converted_values, prediction_text='Quality: {}'.format(decoded_prediction))

               

@app.route('/rfpredict', methods=['POST'])   
def rfpredict():   
    # Extract the input values from the form     
    input_values_rf = {key: int(value) for key, value in request.form.items()}

    # Call your model's predict function with the input features
    prediction_rf = rfmodel.predict([np.array(list(input_values_rf.values()))])
    output_rf = round(prediction_rf[0], 2)
    output_rf = float(output_rf)   

    converted_values_rf = {}

    # Create a dictionary to map radio button values to display names

    # Define the radio button field names
    radio_button_fields_rf = ["Maid Room","Unfurnished","Balcony","Barbecue Area","Built in Wardrobes",
    "Central A/C","Childrens Play Area","Childrens Pool","Concierge","Covered Parking",
    "Kitchen Appliances", "Lobby in Building","Maid Service","Networked","Pets Allowed","Private Garden",
    "Private Gym","Private Jacuzzi","Private Pool","Security","Shared Gym","Shared Pool","Shared Spa",
    "Study","Vastu Compliant","View of Landmark","View of Water","Walk in Closet"]  

    # Iterate through the form values
    for field, value in input_values_rf.items():
     if field in radio_button_fields_rf:
        # Check if the value is in the mapping dictionary
        if value in radio_button_display_names:
            display_name_rf = radio_button_display_names[value]
        else:
            # If not found in the mapping, keep the original value
            display_name_rf = value
        converted_values_rf[field] = display_name_rf
     else:
        converted_values_rf[field] = value       

    # Store the input values and prediction in session variables
    session['input_values_rf'] = input_values_rf
    session['prediction_rf'] = output_rf
    session['converted_values_rf'] = converted_values_rf
 # Store the decoded prediction label   

    # Redirect to the result page 
    return redirect(url_for('show_rf_result'))


@app.route('/rfresult')
def show_rf_result():  
    # Retrieve the input values and decoded prediction from the session
    input_values_rf = session.get('input_values_rf', {})
    output_rf = session.get('prediction_rf', "Unknown")
    converted_values_rf = session.get('converted_values_rf', {})

    # Pass the input values and decoded prediction to the result.html template
    return render_template('resultrf.html', input_values_rf=input_values_rf,converted_values_rf=converted_values_rf, prediction_text_rf='Price: ${}'.format(output_rf))

if __name__ == "__main__":         
    app.run(debug=True)   
    