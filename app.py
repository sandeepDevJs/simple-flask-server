from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to youtube channel yoyo"

@app.route('/hello')
def hello():
    return "Hello bhaiya"


if __name__=='__main__':
    app.run(debug=True)