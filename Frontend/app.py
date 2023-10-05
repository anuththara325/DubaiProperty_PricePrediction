import numpy as np
from flask import Flask, request, render_template, redirect, url_for, session
import pickle

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'q1w2e3r4t5y6'

model = pickle.load(open('Frontend/Model/model.pkl', 'rb'))

prediction_labels = {
    1.0: "Low",
    2.0: "Medium",
    3.0: "High",    
    # Add more mappings as needed
}    

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():   
    # Extract the input values from the form     
    input_values = {key: int(value) for key, value in request.form.items()}

    # Call your model's predict function with the input features
    prediction = model.predict([np.array(list(input_values.values()))])
    output = round(prediction[0], 2)
    output = float(output)     
     
    # Map the numerical prediction to a label
    if output in prediction_labels:
        decoded_prediction = prediction_labels[output]   
    else:
        decoded_prediction = "Unknown"  # Handle the case where the prediction doesn't match any label

    # Store the input values and prediction in session variables
    session['input_values'] = input_values
    session['prediction'] = decoded_prediction  # Store the decoded prediction label

    # Redirect to the result page
    return redirect(url_for('show_result'))

@app.route('/result')
def show_result():
    # Retrieve the input values and decoded prediction from the session
    input_values = session.get('input_values', {})
    decoded_prediction = session.get('prediction', "Unknown")

    # Pass the input values and decoded prediction to the result.html template
    return render_template('result.html', input_values=input_values, prediction_text='Quality: {}'.format(decoded_prediction))

if __name__ == "__main__":
    app.run(debug=True)
