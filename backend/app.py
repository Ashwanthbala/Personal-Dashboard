from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the personal dashboard!"

if __name__ == '__main__':
    app.run(debug=True)