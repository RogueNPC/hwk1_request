from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

if __name__ == '__main__':
    app.run(debug=True)
