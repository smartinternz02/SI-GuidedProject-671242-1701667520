from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict')
def predict():
    return render_template('click_predict.html')

@app.route('/result')
def result():
    # You can pass any necessary data to the result.html template here
    prediction = "Your Prediction"
    total_score = 100
    return render_template('result.html', prediction=prediction, total_score=total_score)

if __name__ == '__main__':
    app.run(debug=True)
