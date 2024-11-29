from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/age', methods= ['GET', 'POST'])
def predict():
    if request.method == 'POST':
        born = int(request.form['born'])
        now = datetime.now().year
        age = now - born
        return render_template('predict.html', age=age, born=born, now=now) 
    return render_template('predict.html', age= None)

if __name__ == '__main__':
    app.run(host='0.0.0.0')