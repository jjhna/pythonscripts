from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Needed for session handling

@app.route('/', methods=['GET', 'POST'])
def index():
    # Default options
    default_options = ['Option A', 'Option B', 'Option C', 'Option D']

    # Initialize session data
    if 'options' not in session:
        session['options'] = default_options.copy()

    if request.method == 'POST':
        selected = request.form.getlist('options')
        new_option = request.form.get('new_option', '').strip()

        # Add new option if it's not empty or a duplicate
        if new_option and new_option not in session['options']:
            session['options'].append(new_option)
            session.modified = True  # Needed to update session data

        return render_template(
            'flasktest2.html',
            options=session['options'],
            selected=selected
        )

    return render_template(
        'flasktest2.html',
        options=session['options'],
        selected=[]
    )

if __name__ == '__main__':
    app.run(debug=True)
