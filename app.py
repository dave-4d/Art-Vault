from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Art Commission Manager"

if __name__ == '__main__':
    app.run(debug=True)