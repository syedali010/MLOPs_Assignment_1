from flask import Flask, request, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load(
    'customer_segmentation_model.pkl'
)


# Two blank lines before the function
@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Gather input features from the form
        gender = request.form['gender']
        age = float(request.form['age'])
        annual_income = float(request.form['annual_income'])
        spending_score = float(request.form['spending_score'])

        # Convert gender to numeric
        gender_numeric = 1 if gender.lower() == 'male' else 0

        # Make prediction using the loaded model
        features = [gender_numeric, age, annual_income, spending_score]

        # Breaking the long line
        prediction = model.predict([features])

        # Removed trailing whitespace from the blank lines
        return render_template('result.html', prediction=prediction[0])

    # Render the input form template
    return render_template('predict.html')


if __name__ == '__main__':
    app.run(port=8081, host="0.0.0.0")
