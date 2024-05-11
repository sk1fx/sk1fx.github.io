from flask import Flask, render_template, url_for, jsonify
import random
import os
import time

app = Flask(__name__)

number=1
game=1

@app.route('/')
def get_image():
    filename = 'static/assets/main.png'
    return render_template('index.html', main=filename)




@app.route('/get', methods=['POST'])
def call_flask_function():
    time.sleep(3)
    global game
    global number
    if number == 1:
        photo = random.choice(os.listdir('static/assets/mines3'))
        new = random.choice(os.listdir('static/assets/mines3'))
        if new != photo:
            new_image='static/assets/mines3/'+new
    if number == 3:
        photo = random.choice(os.listdir('static/assets/mines3'))
        new = random.choice(os.listdir('static/assets/mines3'))
        if new != photo:
            new_image='static/assets/mines3/'+new
    if number == 5:
        photo = random.choice(os.listdir('static/assets/mines5'))
        new = random.choice(os.listdir('static/assets/mines5'))
        if new != photo:
            new_image='static/assets/mines5/'+new
    if number == 7:
        photo = random.choice(os.listdir('static/assets/mines7'))
        new = random.choice(os.listdir('static/assets/mines7'))
        if new != photo:
            new_image='static/assets/mines7/'+new
    game = random.randint(9000,10000)
    game_number = f'ИГРА №{game} - ШАНС {random.randint(70,95)}%'
    return jsonify({'new_image': new_image, 'count': game_number})



@app.route('/plus', methods=['POST'])
def plus_number():
    global number
    if number == 5:
        number = 7
    if number == 3:
        number = 5
    if number == 1:
        number = 3
    return jsonify({'new_number': number})

@app.route('/minus', methods=['POST'])
def minus_number():
    global number
    if number == 3:
        number = 1
    if number == 5:
        number = 3
    if number == 7:
        number = 5
    return jsonify({'new_number': number})

if __name__ == '__main__':
    app.run(debug=True)
