from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, world thank you once again and wish you all the best!'

if __name__ == '__main__':
    app.run()


