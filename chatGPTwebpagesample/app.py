from flask import Flask, render_template, url_for, request, redirect, flash, session

app = Flask(__name__)
# Simple secret key for flashing messages in this sample app.
app.secret_key = 'dev-secret-key'
# Limit upload size to 1MB for CSV uploads
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/page1')
def page1():
    return render_template('page1.html')


@app.route('/page2')
def page2():
    return render_template('page2.html')


@app.route('/page3', methods=['GET', 'POST'])
def page3():
    # Handle form POST without any JavaScript.
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        # Very small server-side validation for the sample.
        if not name or not email:
            flash('Please provide both name and email.', 'error')
            return redirect(url_for('page3'))

        # In a real app you might store the message, send an email, etc.
        flash('Thank you, your message was received.', 'success')
        return redirect(url_for('page3'))

    # On GET, check for any CSV prefill data stored in session and pass to template.
    prefill = session.pop('prefill', None)
    return render_template('page3.html', prefill=prefill)


@app.route('/upload_csv', methods=['POST'])
def upload_csv():
    # Accept a CSV file upload, parse first row (or first data row if headers present)
    uploaded = request.files.get('csvfile')
    if not uploaded or uploaded.filename == '':
        flash('No file selected for upload.', 'error')
        return redirect(url_for('page3'))

    filename = uploaded.filename.lower()
    if not filename.endswith('.csv'):
        flash('Please upload a CSV file (.csv).', 'error')
        return redirect(url_for('page3'))

    try:
        # Read content as text
        data = uploaded.stream.read().decode('utf-8', errors='replace')
        import csv
        rows = list(csv.reader(data.splitlines()))
        if not rows:
            flash('The uploaded CSV is empty.', 'error')
            return redirect(url_for('page3'))

        # Determine if first row looks like headers
        header_row = rows[0]
        lower_hdrs = [c.lower().strip() for c in header_row]
        has_headers = any(h in ('name', 'email', 'message') for h in lower_hdrs) and len(rows) > 1

        # Choose the data row to use
        data_row = rows[1] if has_headers and len(rows) > 1 else rows[0]

        # Mapping: try headers if available, else positional
        prefill = {'name': '', 'email': '', 'message': ''}
        if has_headers:
            idx_map = {h: i for i, h in enumerate(lower_hdrs)}
            if 'name' in idx_map and idx_map['name'] < len(data_row):
                prefill['name'] = data_row[idx_map['name']]
            if 'email' in idx_map and idx_map['email'] < len(data_row):
                prefill['email'] = data_row[idx_map['email']]
            if 'message' in idx_map and idx_map['message'] < len(data_row):
                prefill['message'] = data_row[idx_map['message']]
        else:
            # positional: name,email,message -> indexes 0,1,2
            if len(data_row) > 0:
                prefill['name'] = data_row[0]
            if len(data_row) > 1:
                prefill['email'] = data_row[1]
            if len(data_row) > 2:
                prefill['message'] = data_row[2]

        # Store in session so GET /page3 can pre-populate the form (no JS required)
        session['prefill'] = prefill
        flash('CSV uploaded — form will be populated with parsed values.', 'success')
        return redirect(url_for('page3'))
    except Exception as exc:
        flash('Failed to parse CSV: {}'.format(str(exc)), 'error')
        return redirect(url_for('page3'))


@app.route('/upload_text', methods=['POST'])
def upload_text():
    # Accept a plain text file. Expected formats supported:
    # 1) Key/value style (each line like "name: Alice")
    # 2) Positional lines: first non-empty line = name, second = email, third = message
    uploaded = request.files.get('textfile')
    if not uploaded or uploaded.filename == '':
        flash('No file selected for upload.', 'error')
        return redirect(url_for('page3'))

    fname = uploaded.filename.lower()
    if not (fname.endswith('.txt') or fname.endswith('.text')):
        flash('Please upload a text file (.txt).', 'error')
        return redirect(url_for('page3'))

    try:
        text = uploaded.stream.read().decode('utf-8', errors='replace')
        lines = [l.strip() for l in text.splitlines() if l.strip()]
        prefill = {'name': '', 'email': '', 'message': ''}

        # Try to parse key: value pairs
        kv_parsed = False
        for line in lines:
            if ':' in line:
                parts = line.split(':', 1)
                key = parts[0].strip().lower()
                val = parts[1].strip()
                if key in ('name', 'email', 'message'):
                    prefill[key] = val
                    kv_parsed = True

        if not kv_parsed:
            # fallback to positional mapping
            if len(lines) > 0:
                prefill['name'] = lines[0]
            if len(lines) > 1:
                prefill['email'] = lines[1]
            if len(lines) > 2:
                # join remaining lines as message
                prefill['message'] = '\n'.join(lines[2:])

        session['prefill'] = prefill
        flash('Text file uploaded — form will be populated with parsed values.', 'success')
        return redirect(url_for('page3'))
    except Exception as exc:
        flash('Failed to parse text file: {}'.format(str(exc)), 'error')
        return redirect(url_for('page3'))


@app.route('/page4')
def page4():
    return render_template('page4.html')


if __name__ == '__main__':
    app.run(debug=True)
