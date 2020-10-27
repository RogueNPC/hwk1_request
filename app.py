from flask import Flask
app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/polar_bears')
def favoriteAnimal():
    return 'Polar Bears are cute!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    return f'Wow, {users_animal} are my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_desert(users_dessert):
    return f'How did you know I liked {users_dessert}?'

@app.route('/madlibs/<adjective>/<noun>')
def madlibs(adjective, noun):
    return f'The sitcom about the {noun} never took off, because the pilot was {adjective}.'

if __name__ == '__main__':
    app.run(debug=True)