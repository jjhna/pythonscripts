# Test flask
# cd D:\PythonProject\pythonscripts
# python .\flasktest.py

from flask import Flask, request, render_template
from maindrive.maindrivetemplate import Account

app = Flask(__name__)

@app.route('/frontpage', methods=['GET','POST'])
def frontpage():
    newacc = Account("Tanjiro",69,"Demon","Slayer",{"name": "Tanjiro Kamado","age": 15,"breathing_style": "Water Breathing","rank": "Demon Slayer","sword_color": "Black"})
    if request.method == 'POST':
        textinputbox = request.form['textbox2']
        checkboxbool = 'checkbox1' in request.form
        textbox1result = request.form.get('textbox1')
        if checkboxbool:
            textbox1result += " is the magic word"
        else:
            textbox1result = "Default"
        thisacc = newacc.speak()
        theaddress = newacc.printAddresses()
    return render_template('flasktest.html', resulttextbox1 = textbox1result, resulttextbox2 = textinputbox,thisacc = thisacc, theaddress = theaddress) 

@app.route('/')
def home():
    return render_template('flasktest.html')

if __name__ == '__main__':
    app.run(debug=True)