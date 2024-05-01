import tkinter
import random
import sys
from tkinter import messagebox
from questions import *

ball = 0
answer_count = -1
answer_was = []

class Main_Run_Game(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.window_settings()
        self.main_menu()

    def window_settings(self):
        icon = tkinter.PhotoImage(file='3409496.png')
        self.title('Викторина')
        self.geometry('400x250')
        self.iconphoto(True, icon)
        self.resizable(height=False, width=False)

    def main_menu(self):

        global ball, answer_was, answer_count

        ball = 0
        answer_count = -1
        answer_was = []

        menu_label = tkinter.Label(self, text='Выберите уровень сложности', font=('Arial', 12))
        menu_label.place(x=90, y=10)

        bt_easy = tkinter.Button(self, text='Лёгкий', font=('Arial', 12), width=10, height=2, background='green',
                                 command=lambda: self.mod_game(1))
        bt_easy.place(x=60, y=40)

        bt_normal = tkinter.Button(self, text='Обычный', font=('Arial', 12), width=10, height=2, background='blue',
                                   command=lambda: self.mod_game(2))
        bt_normal.place(x=220, y=40)

        bt_diff = tkinter.Button(self, text='Сложный', font=('Arial', 12), width=10, height=2, background='yellow',
                                 command=lambda: self.mod_game(3))
        bt_diff.place(x=60, y=100)

        bt_expert = tkinter.Button(self, text='Эксперт', font=('Arial', 12), width=10, height=2, background='red',
                                   command=lambda: self.mod_game(4))
        bt_expert.place(x=220, y=100)

        bt_exit = tkinter.Button(self, text='Выход', font=('Arial', 12), width=10, height=2,
                                 command=lambda: self.mod_game(5))
        bt_exit.place(x=139, y=170)

        bt_rools = tkinter.Button(self, text='Правила', font=('Arial', 10), width=6, height=2, background='grey',
                                  command=lambda: self.mod_game(6))
        bt_rools.place(x=20, y=200)

        bt_balls_result = tkinter.Button(self, text='Баллы', font=('Arial', 10), width=6, height=2, background='grey',
                                         command=lambda: self.mod_game(7))
        bt_balls_result.place(x=330, y=200)

    def mod_game(self, mod):

        if mod == 1:
            self.clear_all(1, 2)

        elif mod == 2:
            self.clear_all(2, 2)

        elif mod == 3:
            self.clear_all(3, 2)

        elif mod == 4:
            root_info = messagebox.askyesno(title='Правила', message='В разроботке...')

        elif mod == 5:
            sys.exit()

        elif mod == 6:
            root_info = messagebox.askyesno(title='Правила', message='Правила: \n'
                                                                     '1) Выберите сложность вопросов\n'
                                                                     '\n'
                                                                     '2) Отвечаете на вопрос, выбрав один из вариантов ответов и \n'
                                                                     'нажмите на кнопку слево от ответа.\n'
                                                                     '\n'
                                                                     'Чем сложнее вопрос, тем больше баллов даётся за правильный ответ.\n'
                                                                     'Если ответ не верный, то теряется один балл, не в зависимости от сложности вопроса.\n'
                                                                     'Чтобы выиграть нужно набрать определённое количевство баллов,\n '
                                                                     'нужное количевство зависит от сложности, выбранноё в начале\n'
                                                                     '\n'
                                                                     'Удачи!')

        elif mod == 7:
            root_info = messagebox.askyesno(title='Баллы', message='Баллы за вопрос сложности:\n'
                                                                   'Лёгкий: 1\n'
                                                                   'Обычный: 2\n'
                                                                   'Сложный: 3\n'
                                                                   'Эксперт: 4\n'
                                                                   'Количевство баллов для победы:\n'
                                                                   '\n'
                                                                   'Лёгкая сложность: 6 баллов\n'
                                                                   'Обычная сложность: 9 баллов\n'
                                                                   'Сложная сложность: 15 баллов\n'
                                                                   'Эксперт: 22 баллов')

    def main_question(self):

        global ball, questions, answer_count, answer_was

        # так проще добавлять вопросы
        current_questions = []
        for item in questions['easy']:
            current_questions.append(questions['easy'][item])
        current_question = random.choice(current_questions)

        root_quest = tkinter.Label(self, text=current_question[0], font=('Arial', 10))
        root_quest.place(x=5, y=5)

        # TODO: Лёгкие вопросы
        q = None
        d = None
        for diff in questions:
            for quest in questions[diff]:
                if current_question == questions[diff][quest]:
                    d = diff
                    q = quest


        if current_question in answer_was:
            current_questions.remove(questions[d][q])
            answer_count -= 1
            self.clear_all(1, 2)
        else:
            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                      command=lambda: self.clear_all(1, False, 0, ))
            root_v_1.place(x=80, y=30)
            root_v_1 = tkinter.Label(self, text=questions[d][q][1], font=('Arial', 12))
            root_v_1.place(x=160, y=34)
            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                      command=lambda: self.clear_all(1, True))
            root_v_2.place(x=80, y=70)
            root_v_2 = tkinter.Label(self, text=questions[d][q][2], font=('Arial', 12))
            root_v_2.place(x=160, y=74)
            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                      command=lambda: self.clear_all(1, False))
            root_v_3.place(x=80, y=110)
            root_v_3 = tkinter.Label(self, text=questions[d][q][3], font=('Arial', 12))
            root_v_3.place(x=160, y=114)
            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                      command=lambda: self.clear_all(1, False, ))
            root_v_4.place(x=80, y=150)
            root_v_4 = tkinter.Label(self, text=questions[d][q][4], font=('Arial', 12))
            root_v_4.place(x=160, y=154)
            answer_was.append(current_question)

    def clear_all(self, mod_g, mod_ot, question_easy_n=1, question_normal=1):

        global answer_count, questions_easy, questions_normal, answer_was

        answer_count += 1

        for widjet in self.winfo_children():
            widjet.destroy()

        if answer_count == 10:
            if mod_g == 1:
                self.win_or_lose_result(1)
                self.main_menu()

            elif mod_g == 2:
                self.win_or_lose_result(2)
                self.main_menu()

            elif mod_g == 3:
                self.win_or_lose_result(3)
                self.main_menu()

            elif mod_g == 4:
                self.win_or_lose_result(4)
                self.main_menu()


        else:
            if mod_g == 1:
                if mod_ot:
                    self.otvet_on_quest(1)
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(-1)
                self.main_question()

            elif mod_g == 2:
                if mod_ot:
                    self.otvet_on_quest(2)
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(-1)
                self.main_question()

            elif mod_g == 3:
                if mod_ot:
                    self.otvet_on_quest(3)
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(-1)
                self.main_question()

            elif mod_g == 4:
                if mod_ot:
                    self.otvet_on_quest(4)
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(-1)
                self.main_question()

            else:
                if mod_ot:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(0)


    def mod_game_2(self):
        sys.exit()

    # TODO: Проверка ответа
    def otvet_on_quest(self, pl_b):

        global ball

        ball += pl_b

        if ball < 0:
            ball = 0
        print(ball)



    def win_or_lose_result(self, mod_ga):

        root = tkinter.Tk()
        root.title('Викторина')
        root.geometry('200x150')

        global ball, answer_was

        if mod_ga == 1:
            if ball >= 6:
                text = 'Поздравляю!\n' \
                       'Вы победили!'
            else:
                text = 'Проигрыш!\n'

        elif mod_ga == 2:
            if ball >= 9:
                text = 'Поздравляю!\n' \
                       'Вы победили!'
            else:
                text = 'Проигрыш!\n' \

        elif mod_ga == 3:
            if ball >= 15:
                text = 'Поздравляю!\n' \
                       'Вы победили!'
            else:
                text = 'Проигрыш!\n'

        elif mod_ga == 4:
            if ball >= 22:
                text = 'Поздравляю!\n' \
                       'Вы победили!'
            else:
                text = 'Проигрыш!\n'

        else:
            text = 'Проигрыш!\n'

        label = tkinter.Label(root, text=text, font=('Arial', 12))
        label.place(x=50, y=10, width=100)

        button = tkinter.Button(root, text='Выход', font=('Arial', 18),  command=self.mod_game_2, )
        button.place(x=50, y=50, width=100)


app = Main_Run_Game()
app.mainloop()
