from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Available choices
choices = ['Rock', 'Paper', 'Scissors']

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'Rock' and computer_choice == 'Scissors') or
        (user_choice == 'Scissors' and computer_choice == 'Paper') or
        (user_choice == 'Paper' and computer_choice == 'Rock')
    ):
        return "You win!"
    else:
        return "Computer wins!"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_choice = request.form['choice']
        computer_choice = random.choice(choices)
        result = determine_winner(user_choice, computer_choice)
        return render_template('index.html', user_choice=user_choice, computer_choice=computer_choice, result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
