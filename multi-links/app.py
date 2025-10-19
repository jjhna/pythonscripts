from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    a1 = {"name": "Alice", "age": 25, "city": "New York"}
    return render_template('about.html', a1 = a1)

if __name__ == '__main__':
    app.run(debug=True)