from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send():
    data = request.form['data']
    print(f"Received data: {data}")
    return "Success", 200

@app.route('/send-editor-content', methods=['POST'])
def send_editor_content():
    editor_content = request.form['data']
    print(f"Received editor content: {editor_content}")
    # Process the editor content here (e.g., execute Python code)
    # ...
    response = "Processed editor content"
    return response, 200

