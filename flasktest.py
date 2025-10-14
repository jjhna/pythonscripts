# Test flask
# cd D:\PythonProject\pythonscripts
# python .\flasktest.py

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/frontpage', methods=['GET','POST'])
def frontpage():
    if request.method == 'POST':
        textinputbox = request.form['textbox2']
        checkboxbool = 'checkbox1' in request.form
        textbox1result = request.form.get('textbox1')
        if checkboxbool:
            textbox1result += " is the magic word"
        else:
            textbox1result = "Default"
    return render_template('flasktest.html', resulttextbox1 = textbox1result, resulttextbox2 = textinputbox) 

@app.route('/')
def home():
    return render_template('flasktest.html')

if __name__ == '__main__':
    app.run(debug=True)