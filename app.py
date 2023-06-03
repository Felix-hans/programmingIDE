from flask import Flask, render_template, request
import getGPTResponse

import os
import executeCode


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send():
    userPrompt = request.form['data']
    print(f"Received data: {userPrompt}")

    response = getGPTResponse.main(userPrompt)

    return response, 200


@app.route('/send-editor-content', methods=['POST'])
def send_editor_content():
    editor_content = request.form['data']
    print(f"Received editor content: {editor_content}")
    
    response = executeCode.main(editor_content)
    
    return response, 200


