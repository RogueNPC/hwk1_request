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

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if (number1.isdigit() == True and number2.isdigit() == True):
        total = int(number1) * int(number2)
        return f'{number1} times {number2} is {total}'
    else:
        return 'Invalid inputs. Please try again by entering 2 numbers!'

@app.route('/sayntimes/<word>/<n>')
def sayntimes(word, n):
    if (word.isalpha() == True and n.isdigit() == True):
        return (word + ' ') * int(n)
    else:
        return 'Invalid input. Please try again by entering a word and a number!'

if __name__ == '__main__':
    app.run(debug=True)