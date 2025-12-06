from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return send_from_directory('home', 'home.html')

@app.route('/form1')
def form1():
    return send_from_directory('form1', 'form1.html')

@app.route('/settings')
def settings():
    return send_from_directory('settings', 'settings.html')


@app.route('/navbar/<path:filename>')
def navbar_files(filename):
    # Serve the reusable navbar HTML (and any files placed in navbar/)
    return send_from_directory('navbar', filename)

if __name__ == '__main__':
    app.run(debug=True)
