import json
import random

trivia_file = open('Apprentice_TandemFor400_Data.json',)

data = json.load(trivia_file)

questions = []
score = 0

class trivia_question:
    def __init__(self, question, incorrect, correct):
        self.question = question
        self.answers = incorrect + [correct]
        self.correct = correct

random.shuffle(data)

for i in data[:10]:
    question = trivia_question(i['question'], i['incorrect'], i['correct'])
    questions.append(question.__dict__)

def prompt_for_answer():
    global score
    user_answer = input("Please select an answer... ")

    if user_answer in answer_key_list:
        if answers_dict[user_answer] == question['correct']:
            print("Correct!")
            score += 1
            
        else:
            print(f"So close! The answer was {question['correct']}")

        print(f"Your score is now {score}/10")

    else:
        print("Oops, not a valid answer! Try again ")
        prompt_for_answer(score)

input("Welcome to Tandem for 400! Press enter to continue... ")

for question in questions:
    print(question['question'])
    random.shuffle(question['answers'])

    answer_key_list = ['A','B','C','D']

    answers_dict = dict(zip(answer_key_list, question['answers']))

    for key, value in answers_dict.items():
        print(f'{key}: {value}')

    print("")
    prompt_for_answer()

trivia_file.close()

print(f"Your final score is {score}/10! ")