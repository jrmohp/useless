from celery import Celery
from flask import Flask, request, jsonify, session
from celery.result import AsyncResult
from celery_tasks import process_pdf_task, celery
from custom_functions import read_sample_pdf_pages
from flask_session import Session


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


# Configure Celery
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'



# Initialize Celery
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@app.route('/process-pdf', methods=['POST'])
def process_pdf():
    if 'file' not in request.files:
        return 'No file uploaded.', 400

    file = request.files['file']
    file_path = 'path/to/save/your/pdf/file.pdf'
    file.save(file_path)

    # Trigger the Celery task asynchronously
    task = process_pdf_task.apply_async(args=[file_path])

    return jsonify({'task_id': task.id}), 202

@app.route('/progress/<task_id>', methods=['GET'])
def check_progress(task_id):
    task = celery.AsyncResult(task_id)
    if task.state == 'PENDING':
        response = {
            'state': task.state,
            'progress': 0
        }
    elif task.state == 'PROGRESS':
        response = {
            'state': task.state,
            'progress': task.info.get('progress', 0)
        }
    else:
        response = {
            'state': task.state,
            'progress': 100,
            'result': task.result
        }
    return jsonify(response)

@app.route('/')
def index():
    session['key'] = 'value'  # Set a sample session variable
    response = app.make_response(render_template('index.html'))
    response.set_cookie('session', session.sid, httponly=True)  # Set session cookie
    return response


@app.route('/your-endpoint')
def your_endpoint():
    session_id = request.headers.get('Session-ID')
    session_interface = app.session_interface
    session = session_interface.open_session(app, session_id)


@app.route('/pdfsampledata')
def process_pdf():
    if 'pdf' not in session:
        return 'No PDF file stored in session. Upload a PDF First.', 400

    num_pages = 50
    file_path = session['pdf']

    text = read_sample_pdf_pages(file_path, num_pages)

    return text, 200

@app.route('/logout')
def logout():
    session.pop('username', None)
    response = make_response(redirect('/'))
    response.set_cookie('session_id', '', expires=0)  # Clear session ID cookie
    return response



@app.route('/process_marker', methods=['POST'])
def process_marker():
    marker = request.form['marker']

    if 'text_data' not in session:
        return jsonify({'error': 'No text data stored in session. Upload a file first.'}), 400

    text_data = session['text_data']
    lines = text_data.split('\n')

    result = find_lines_around_marker(lines, marker)

    if 'error' in result:
        return jsonify(result), 404

    return jsonify(result)



def find_lines_around_marker(lines, marker):
    result = {'marker': marker, 'lines': []}
    line_index = None

    for i, line in enumerate(lines):
        if marker in line:
            line_index = i
            break

    if line_index is None:
        result['error'] = f"Marker '{marker}' not found in the text data."
    else:
        start = max(0, line_index - 5)
        end = min(len(lines), line_index + 6)

        if start > line_index:
            start = line_index
        if end <= line_index + 1:
            end = min(line_index + 2, len(lines))

        for i, line in enumerate(lines[start:end]):
            relative_index = i - (line_index - start)
            result['lines'].append({'line': line, 'relative_index': relative_index})

    return result




@app.route('/split_segments', methods=['POST'])
def split_segments():
    if 'text_data' not in session:
        return jsonify({'error': 'No text data stored in session. Upload a file first.'}), 400

    text_data = session['text_data']
    lines = text_data.split('\n')

    marker_line = request.form.get('marker_line')
    marker_relative_index = int(request.form.get('marker_relative_index'))

    segments = split_text_segments(lines, marker_line, marker_relative_index)

    return jsonify({'segments': segments})


def split_text_segments(lines, marker_line, marker_relative_index):
    segments = []
    current_segment = []

    for i, line in enumerate(lines):
        if line == marker_line and i - marker_relative_index == 0:
            if current_segment:
                segments.append(current_segment)
                current_segment = []
        current_segment.append(line)

    if current_segment:
        segments.append(current_segment)

    return segments



