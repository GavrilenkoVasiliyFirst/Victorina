import tkinter
import random

ball = 0
def main_question_easy():

    global ball

    questions = {'easy':
                     {'q_1': ['Сколько пешек у одного игрока в шахматах?', '4', '8', '10', '16', 2],
                      'q_2': ['Самое большое млекопитающее в мире?', 'Слон', 'Лошадь', 'Кит', 'Медведь', 3],
                      'q_3': ['Сколько планет в солнечной системе?', '7', '8', '9', '10', 2],
                      }
                 }

    questions_easy = [questions['easy']['q_1'][0], questions['easy']['q_2'][0], questions['easy']['q_3'][0]]
    question_easy = random.choice(questions_easy)
    print(question_easy)

    #Первый вопрос
    if question_easy == questions['easy']['q_1'][0]:
        print(f"1. {questions['easy']['q_1'][1]}")
        print(f"2. {questions['easy']['q_1'][2]}")
        print(f"3. {questions['easy']['q_1'][3]}")
        print(f"4. {questions['easy']['q_1'][4]}")
        otvet = input('\nВведите номер правильного ответа:  ')

        if int(otvet) == questions['easy']['q_1'][-1]:
            ball += 1
        else:

            if ball > 0:
                ball -= 1
            else:
                pass

    #Второй вопрос
    elif question_easy == questions['easy']['q_2'][0]:
        print(f"1. {questions['easy']['q_2'][1]}")
        print(f"2. {questions['easy']['q_2'][2]}")
        print(f"3. {questions['easy']['q_2'][3]}")
        print(f"4. {questions['easy']['q_2'][4]}")
        otvet = input('\nВведите номер правильного ответа:  ')

        if int(otvet) == questions['easy']['q_2'][-1]:
            ball += 1
        else:

            if ball > 0:
                ball -= 1
            else:
                pass

    elif question_easy == questions['easy']['q_3'][0]:
        print(f"1. {questions['easy']['q_3'][1]}")
        print(f"2. {questions['easy']['q_3'][2]}")
        print(f"3. {questions['easy']['q_3'][3]}")
        print(f"4. {questions['easy']['q_3'][4]}")
        otvet = input('\nВведите номер правильного ответа:  ')

        if int(otvet) == questions['easy']['q_3'][-1]:
            ball += 1
        else:

            if ball > 0:
                ball -= 1
            else:
                pass

    print('Ответ получен\n')
