from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/math', methods = ['POST'])
def math_add():
    if(request.method == 'POST'):
        operation = request.form['operation']
        number1 = int(request.form['number1'])
        number2 = int(request.form['number2'])
        
        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        else:
            result = number1 / number2

        return render_template("result.html",result= round(result,2))

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5000)