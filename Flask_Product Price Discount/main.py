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
        number3 = int(request.form['number3'])
        number4 = int(request.form['number4'])
        number5 = int(request.form['number5'])
        number6 = int(request.form['number6'])
        
        result = number1 + number2 + number3 + number4 + number5 + number6

        if 0 <=result <= 999:
            result =  result
        elif 1999 >= result >= 1000:
            result =  result - (result*10/100)
        elif 1001 <= result <= 2000:
            result = result - (result*20/100)
        else:
            result = result - (result*30/100)

        return render_template("result.html",result= int(result))

if __name__=="__main__":
    app.run(host="0.0.0.0",port = 5000)