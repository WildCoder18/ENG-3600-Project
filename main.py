from flask import Flask, render_template, jsonify
import random


questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["Paris", "Berlin"]
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "choices": ["Mars", "Venus"]
    },
    # Add more questions as needed
]

app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')

@app.route('/Prologue')
def Prologue():
    return render_template('Prologue.html')

@app.route('/Prologue_2')
def Prologue_2():
    return render_template('Prologue_2.html')

@app.route('/Game_Section_1')
def Game_Section_1():
    return render_template('Game_Section_1.html')

@app.route('/get_random_question', methods=['GET'])
def get_random_question():
    # Select a random question from the list
    random_question = random.choice(questions)
    return jsonify(random_question)


if __name__ == '__main__':
    app.run(debug=True)