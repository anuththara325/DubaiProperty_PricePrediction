import numpy as np
from flask import Flask, request, render_template, redirect, url_for, session
import pickle

app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = 'q1w2e3r4t5y6'

model = pickle.load(open('Frontend/Model/model.pkl', 'rb'))

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

    # Store the input values and prediction in session variables
    session['input_values'] = input_values
    session['prediction'] = output

    # Redirect to the result page
    return redirect(url_for('show_result'))

@app.route('/result')
def show_result():
    # Retrieve the input values and prediction from the session
    input_values = session.get('input_values', {})
    output = session.get('prediction', None)

    # Pass the input values and prediction to the result.html template
    return render_template('result.html', input_values=input_values, prediction_text='Quality: {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
