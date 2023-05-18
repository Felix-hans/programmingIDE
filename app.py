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

if __name__ == '__main__':
    app.run(debug=True)
