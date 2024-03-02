import math

def user_info (name, age, degree):
    return '{} of {} holding a {} degree'.format(name,age,degree)

def quiz_game():
    questions = [
        "1. What is capital of France",
        "2. Who is the author of Game of Thrones"
        "3. What the chemical symbol of water" 
                 ]
    answers = [
        "Paris",
        "Robert Greene"
        "H2O"
    ]
    user_answers = list()
    points = 0

    for i in range(len(questions)):
        print(questions[i])
        user_input = input(f"Enter the answer for {i+1}:\n")
        if(user_input == answers[i]):
            print("Correct")
            points += 1
        else:
            print("Incorrect")
            continue
        user_answers.append(user_input)
    print("The answers have been stored")
    return user_answers
    
def display_results(user_answers):
    print("Quiz Details")
    for i in range(len(user_answers)):
        print(user_answers)
    
    
name = input('Enter your name:\n')
age = input ('Enter your age:\n')
degree = input ('Enter your degree:\n')
answer = quiz_game()

info = user_info(name,age,degree)
print(info)
display_results(answer)


