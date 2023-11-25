from flask import Flask, render_template, jsonify
import random


characters_data = {
    'Chijioke': {
        'image': 'static/Used_Images/Chijioke_Character.png',
        'name': 'Chijioke (Warrior)',
        'questions': ['Azu! Reports have come in that a rival village is planning a surprise attack. How should we prepare our defense?', 
                      'The neighboring village challenges the prowess of our warriors in a martial arts competition. How do we respond to uphold our village''s honor?', 
                      'The village is facing internal strife, and some warriors are questioning your leadership. How will you address the dissent among the ranks?',
                      'A sacred relic, crucial to our warriors'' spiritual strength, has been stolen. How do we retrieve it and restore the morale of our warriors?',
                      'The training of young warriors is falling behind schedule, affecting our overall readiness for potential conflicts. How should we intensify the training regimen?',
                      'Elder Azu, a women in our tribe has dared to now acknowledge me and show me respect as the great warrior of our tribe! We should get rid of her and give her belongings to the rest of the village!',
                      ],
        
        'choices': [['Send emissaries to the rival village, expressing a desire for peaceful resolution.', 'Mobilize our warriors for a preemptive strike to discourage the attack.'],
                    
                    ['Politely decline and focus on maintaining peaceful relations between the villages.', 'Select our best warriors for a fierce competition to assert our dominance.'],
                    
                    ['Call a council of respected elders and warriors to address grievances and seek a diplomatic resolution.', 'Confront the dissenting warriors directly and assert your authority through a traditional display of strength.'],
                    
                    ['Convene a gathering of village leaders to discuss negotiations for the safe return of the sacred item.', 'Launch a covert mission to infiltrate the rival village and recover the stolen relic.'],
                    
                    ['Seek guidance from seasoned warriors and introduce innovative training methods to keep the young warriors engaged.', 'Implement a strict and rigorous training routine to instill discipline and resilience.'],
                    
                    ['Tell Chijioke put aside your pride and leave the women be.', 'Give Chijioke the go ahead to follow-through in his plans.']
                    ]
    },
    
   
    # Add more characters as needed...
}
    # Add more characters as needed...


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
    
@app.route('/get_random_game_data')
def get_random_game_data():
    # Randomly select a character
    character_name = random.choice(list(characters_data.keys()))
    character_info = characters_data[character_name]

    # Randomly select a question and choices for the character
    question_index = random.randint(0, len(character_info['questions']) - 1)
    question = character_info['questions'][question_index]
    choices = character_info['choices'][question_index]

    # Prepare the response data
    response_data = {
        'character': {'name': character_info['name'], 'image': character_info['image']},
        'question': question,
        'choices': choices
    }

    return jsonify(response_data)



if __name__ == '__main__':
    app.run(debug=True)