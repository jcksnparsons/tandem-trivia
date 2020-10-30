import json
import random

# Gets data from the JSON file
trivia_file = open('Apprentice_TandemFor400_Data.json',)

data = json.load(trivia_file)

trivia_file.close()

questions = []
score = 0

class trivia_question:
    """Class that contains information on each question"""
    def __init__(self, question, incorrect, correct):
        self.question = question
        self.answers = incorrect + [correct]
        self.correct = correct

random.shuffle(data)

# Grabs 10 random questions from the file, creates trivia_question instances from each question, and adds each one to our question list
for q_object in data[:10]:
    question = trivia_question(q_object['question'], q_object['incorrect'], q_object['correct'])
    questions.append(question)

# Main function
def prompt_for_answer():
    # Yes, I know, not my favorite solution to use the global keyword, but it made for the cleanest and most readable solution
    global score
    user_answer = input("Please select an answer... ")
    print("")

    # If the input is a key in the answers dictionary, it evaluates to see if the value associated 
    # with that key is equal to the 'correct' attribute on the question instance. 
    # If true, it adds one to the score and continues through the loop. 
    # If false, the score doesn't change and it continues through the loop.

    try:
        if answers_dict[int(user_answer)] == question.correct:
            print("Correct!")
            score += 1
            
        else:
            print(f"So close! The answer was {question.correct}")

        print(f"Your score is now {score}/10")
        print("")
    
    # Error handling. If the user input is not a valid key on our answer dict, the function is invoked again on the question. Woo recursive strategy!
    except:
        print("Oops, not a valid answer! Try again ")
        prompt_for_answer()

input("Welcome to Tandem for 400! Press any key to continue... ")
print("")


for question in questions:
    print(question.question)
    random.shuffle(question.answers)

    # creates a list of answer keys based on how many answers there are for each question. This allows for up to 10 answers on each question
    answer_key_list = []
    for i in range(len(question.answers)):
        answer_key_list.append(i)

    # combines the answers for each question and the newly created answer key list and combines them 
    # into a new dict where our keys have values that are options for question answers
    answers_dict = dict(zip(answer_key_list, question.answers))

    # prints each option for answers
    for key, value in answers_dict.items():
        print(f'{key}: {value}')

    print("")
    # invokes the above answer prompt function
    prompt_for_answer()


# Once the loop is completed, prints out the final score
print(f"Your final score is {score}/10! ")