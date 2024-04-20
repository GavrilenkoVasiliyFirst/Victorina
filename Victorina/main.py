import tkinter
import random
import sys
from tkinter import messagebox

# TODO: Вопросы

answer_count = -1
ball = 0

questions = {'easy':
                     {'q_1': ['Сколько пешек у одного игрока в шахматах?', '4 пешки', '8 пешек', '10 пешек', '16 пешек', 2],
                      'q_2': ['Самое большое млекопитающее в мире?', 'Слон', 'Лошадь', 'Кит', 'Медведь', 3],
                      'q_3': ['Сколько планет в солнечной системе?', '7 планет', '8 планет', '9 планет', '10 планет', 2],
                      'q_4': ['Какая наука изучает растения?', 'Астрономя', 'Цитология', 'Зоология', 'Ботаника', 4],
                      'q_5': ['Сколько времени рыбачил старик из сказки о Золотой рыбке?', '33 года', '33 месяца', '43 года', '43 месяца', 1],
                      'q_6': ['Самый большой кот на планете, это кот породы...', 'Британский', 'Мэйн-кун', 'Чито', 'Тигр', 4],
                      'q_7': ['Единственное млекопитающее, которое умеет летать, это...', 'Летучая мышь', 'Пингвин', 'Аэротитан', 'Тапежара', 1],
                      'q_8': ['У каких пород котов нет шерсти?', 'Сиамская', 'Шантильи-тиффани', 'Сфинкс', 'Саванна', 3],
                      'q_9': ['Имя какого волшебника нельзя называть?', 'Волен-Де-Морт', 'Баба-Яга', 'Бастинда', 'Снежная Королева', 1],
                      'q_10': ['На каждый Новый Год по традиции пересматривают фильм', 'Чарли и шоколадная фабрика', 'Один дома', 'Аватар', 'Полярный Экспресс', 2],
                      'q_11': ['Какое самое медленное животное в мире?', 'Черепаха', 'Змея', 'Ленивец', 'Хамелеон', 3],
                      'q_12': ['Какой самый глубокий океан?', 'Атлантический', 'Индийский', 'Северный ледовитый', 'Тихий', 4]
                      },
            'normal':
                {'q_1': ['Кто открыл электричевство?', 'Бенджамин Франклин', 'Джеёмс Масквелл', 'Никола Тесла', 'Галилео Галилей', 1],
                 'q_2': ['В каой стране находится самый высокий водопад Европы?', 'Норвегия', 'Исландия', 'Швеция', 'Финляндия', 1],
                 'q_3': ['Как называется самая длинная горная цепь в Южной Америке?', 'Анды', 'Альфы', 'Пампа', 'Евразийская степь', 1],
                 'q_4': ['Чему равна сумма числа пи(n) и Коэффициент ускорения свободног падения(g), если они оба округлены до сотых?', '13,06', '13,96', '12,88', '12,94', 4],
                 'q_5': ['Как зовут трёхглавую собаку Хагрида, охраняющую камень в Гарри Поттере?', 'Добби', 'Пушистый', 'Горыныч', 'Музыкант', 2],
                 'q_6': ['Какой знак зодака относится к 1 апреля?', 'Водолей', 'Овен', 'Стрелец', 'Рыбы', 2],
                 'q_7': ['У какого химического элемнта наибольшая электроотрицательнось?', 'У кислорода(О)', 'У фтора(F)', 'У золота(Au)', 'У гелия(He)', 2],
                 'q_8': ['Крупнейший производитель кофе мира это...', 'Вьетнам', 'Колумбия', 'Индонезия', 'Бразилия', 4],
                 'q_9': ['Какой из известных композмтров был глухим?', 'Бах', 'Моцарт', 'Бетховин', 'Гендель', 3],
                 'q_10': ['В каком году Плутоний стал официально считаться карликовой планетой', '2001', '2004', '2006', '2008', 3],
                 'q_11': ['Солнце состоит из водорода(H) на...', '81%', '90%', '92%', '98%', 3],
                 'q_12': ['Сколько полевых игроков в команде по американскому футболу?', '8 игроков', '9 игроков', '10 игроков', '11 игроков', 4]
                 },
             'diff':
                 {'q_1': ['Дебют в шахматах, начинающиеся ходами королевской пешки из е4 в е6', 'Францущская защита', 'Коготь бобра', 'Скандинавская защита', 'Дебют Нимцовича', 1],
                  'q_2': ['Какой термометр появился первым?', 'Жидкостный', 'Механический', 'Оптический', 'Химический', 1],
                  'q_3': ['', '', '', '', '', 1],

                 }
             }

class Main_Run_Game(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.window_settings()
        self.main_menu()

    def window_settings(self):
        self.title('Викторина')
        self.geometry('400x250')
        self.resizable(height=False, width=False)


    def main_menu(self):

        # TODO: Менюшка
        menu_label = tkinter.Label(self, text='Выберите уровень сложности', font=('Arial', 12))
        menu_label.place(x=90, y=10)

        bt_easy = tkinter.Button(self, text='Лёгкий', font=('Arial', 12), width=10, height=2, background= 'green', command=lambda: self.mod_game(1))
        bt_easy.place(x=60, y=40)

        bt_normal = tkinter.Button(self, text='Обычный', font=('Arial', 12), width=10, height=2, background='blue', command=lambda: self.mod_game(2))
        bt_normal.place(x=220, y=40)

        bt_diff = tkinter.Button(self, text='Сложный', font=('Arial', 12), width=10, height=2, background='yellow', command=lambda: self.mod_game(3))
        bt_diff.place(x=60, y=100)

        bt_expert = tkinter.Button(self, text='Эксперт', font=('Arial', 12), width=10, height=2, background='red', command=lambda: self.mod_game(4))
        bt_expert.place(x=220, y=100)

        bt_exit = tkinter.Button(self, text='Выход', font = ('Arial', 12), width = 10, height=2, command=lambda: self.mod_game(5))
        bt_exit.place(x=139, y=170)

        bt_rools = tkinter.Button(self, text='Правила', font=('Arial', 10), width=6, height=2, background='grey', command=lambda: self.mod_game(6))
        bt_rools.place(x=20, y=200)

        bt_balls_result = tkinter.Button(self, text='Баллы', font=('Arial', 10), width=6, height=2, background='grey', command=lambda: self.mod_game(7))
        bt_balls_result.place(x=330, y=200)






    def mod_game(self, mod):

        if mod == 1:
            self.clear_all(1, True)

        elif mod == 2:
            root_info = messagebox.askyesno(title='Правила', message='В разроботке...')

        elif mod == 3:
            root_info = messagebox.askyesno(title='Правила', message='В разроботке...')

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


    def main_question_easy(self):

        global ball

        questions_easy = [questions['easy']['q_1'][0], questions['easy']['q_2'][0], questions['easy']['q_3'][0],
                          questions['easy']['q_4'][0], questions['easy']['q_5'][0], questions['easy']['q_6'][0],
                          questions['easy']['q_7'][0], questions['easy']['q_8'][0], questions['easy']['q_9'][0],
                          questions['easy']['q_10'][0], questions['easy']['q_11'][0], questions['easy']['q_12'][0]]
        question_easy = random.choice(questions_easy)
        root_quest = tkinter.Label(self, text=question_easy, font=('Arial', 10))
        root_quest.place(x=5, y= 5)

        # TODO: Лёгкий вопросы

        #1
        if question_easy == questions['easy']['q_1'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_1'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_1'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_1'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_1'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_1']


        #2
        elif question_easy == questions['easy']['q_2'][0]:
            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_2'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_2'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_2'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_2'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_2']


        #3
        elif question_easy == questions['easy']['q_3'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_2'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_3'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_3'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_3'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_3']


        #4
        elif question_easy == questions['easy']['q_4'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_4'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_4'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_4'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_4'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_4']

        #5
        elif question_easy == questions['easy']['q_5'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_5'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow',  command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_5'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_5'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_5'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_5']

        #6
        elif question_easy == questions['easy']['q_6'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_6'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_6'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_6'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_6'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_6']

        #7
        elif question_easy == questions['easy']['q_7'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_7'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_7'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_7'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_7'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_7']

        #8
        elif question_easy == questions['easy']['q_8'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_8'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_8'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_8'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_8'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_8']

        #9
        elif question_easy == questions['easy']['q_9'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_9'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_9'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_9'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_9'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_9']

        #10
        elif question_easy == questions['easy']['q_10'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_10'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_10'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_10'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_10'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_10']

        #11
        elif question_easy == questions['easy']['q_11'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_11'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_11'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_11'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_11'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_11']

        #12
        elif question_easy == questions['easy']['q_12'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(1,False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['easy']['q_12'][1], font=('Arial', 12))
            root_v_1.place(x=120, y= 34)

            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(1,False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['easy']['q_12'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(1,False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['easy']['q_12'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command=lambda: self.clear_all(1,True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['easy']['q_12'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['easy']['q_12']


    def main_question_normal(self):
        #TODO: Обычные вопросы

        global ball

        questions_normal = [questions['normal']['q_1'][0], questions['normal']['q_2'][0], questions['normal']['q_3'][0],
                          questions['normal']['q_4'][0], questions['normal']['q_5'][0], questions['normal']['q_6'][0],
                          questions['normal']['q_7'][0], questions['normal']['q_8'][0], questions['normal']['q_9'][0],
                          questions['normal']['q_10'][0], questions['normal']['q_11'][0], questions['normal']['q_12'][0]]
        question_normal = random.choice(questions_normal)
        root_quest = tkinter.Label(self, text=question_normal, font=('Arial', 10))
        root_quest.place(x=5, y=5)


        if questions_normal == questions['normal']['q_1'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_1'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_1'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_1'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_1'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_1']


        elif question_normal == questions['normal']['q_2'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_2'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_2'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_2'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_2'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_2']


        elif question_normal == questions['normal']['q_3'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, True))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_3'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_3'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_3'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_3'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_3']


        elif question_normal == questions['normal']['q_4'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_4'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_4'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_4'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_4'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_4']


        elif question_normal == questions['normal']['q_5'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_5'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_5'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_5'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_5'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_5']


        elif question_normal == questions['normal']['q_6'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_6'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_6'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_6'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_6'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_6']


        elif question_normal == questions['normal']['q_7'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_7'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, True))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_7'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_7'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_7'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_7']


        elif question_normal == questions['normal']['q_8'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_8'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_8'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_8'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_8'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_8']


        elif question_normal == questions['normal']['q_9'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_9'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_9'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_9'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_9'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_9']


        elif question_normal == questions['normal']['q_10'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_10'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_10'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_10'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_10'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_10']


        elif question_normal == questions['normal']['q_11'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2,2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_11'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_11'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, True))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_11'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, False))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_11'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_11']


        elif question_normal == questions['normal']['q_12'][0]:

            root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background = 'red', command=lambda: self.clear_all(2, False))
            root_v_1.place(x=60, y= 30)
            root_v_1 = tkinter.Label(self, text=questions['normal']['q_12'][1], font=('Arial', 12))
            root_v_1.place(x=120, y=34)


            root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background = 'yellow', command=lambda: self.clear_all(2, False))
            root_v_2.place(x=60, y= 70)
            root_v_2 = tkinter.Label(self, text=questions['normal']['q_12'][2], font=('Arial', 12))
            root_v_2.place(x=120, y= 74)

            root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background = 'blue', command=lambda: self.clear_all(2, False))
            root_v_3.place(x=60, y= 110)
            root_v_3 = tkinter.Label(self, text=questions['normal']['q_12'][3], font=('Arial', 12))
            root_v_3.place(x=120, y= 114)

            root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background = 'green', command= lambda: self.clear_all(2, True))
            root_v_4.place(x=60, y= 150)
            root_v_4 = tkinter.Label(self, text=questions['normal']['q_12'][4], font=('Arial', 12))
            root_v_4.place(x=120, y= 154)

            del questions['normal']['q_12']
            
            
    def clear_all(self, mod_g, mod_ot):

        global answer_count

        answer_count += 1

        for widjet in self.winfo_children():
            widjet.destroy()

        if answer_count == 11:
            if mod_g == 1:
                self.win_or_lose_result(1)

            elif mod_g == 2:
                self.win_or_lose_result(2)

            elif mod_g == 3:
                self.win_or_lose_result(3)

            elif mod_g == 4:
                self.win_or_lose_result(4)


        else:
            if mod_g == 1:
                if mod_ot:
                    self.otvet_on_quest(1)
                    self.main_question_easy()
                else:
                    self.otvet_on_quest(-1)
                    self.main_question_easy()

            elif mod_g == 2:
                if mod_ot:
                    self.otvet_on_quest(2)
                    self.main_question_normal()
                else:
                    self.otvet_on_quest(-1)
                    self.main_question_normal()

            elif mod_g == 3:
                if mod_ot:
                    self.otvet_on_quest(3)
                else:
                    self.otvet_on_quest(-1)

            elif mod_g == 4:
                if mod_ot:
                    self.otvet_on_quest(4)
                else:
                    self.otvet_on_quest(-1)

            else:
                if mod_ot:
                    self.otvet_on_quest(0)
                else:
                    self.otvet_on_quest(0)

                    

            



    # TODO: Проверка ответа
    def otvet_on_quest(self, pl_b):

        global ball


        ball += pl_b
        print(ball)

    def win_or_lose_result(self, mod_ga):

        root = tkinter.Tk()
        root.title('Викторина')
        root.geometry('400x250')

        global ball

        if mod_ga == 1:
            if ball >= 6:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы победили!'
            else:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы не собрали нужное количевство очков, но Вы можете попробовать ещё раз!'

        elif mod_ga == 2:
            if ball >= 6:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы победили!'
            else:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы не собрали нужное количевство очков, но Вы можете попробовать ещё раз!'

        elif mod_ga == 3:
            if ball >= 6:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы победили!'
            else:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы не собрали нужное количевство очков, но Вы можете попробовать ещё раз!'

        elif mod_ga == 4:
            if ball >= 6:
                text = 'Поздравляю!\n' \
                       '\n' \
                       'Вы победили!'
            else:
                text = 'Проигрыш!\n' \
                       '\n' \
                       'Вы не собрали нужное количевство очков, но Вы можете попробовать ещё раз!'

        else:
            text = 'Проигрыш!\n' \
                   '\n' \
                   'Вы не собрали нужное количевство очков, но Вы можете попробовать ещё раз!'

        # TODO: Сложности 3 сделать по 12 вопросов, менюшка


app = Main_Run_Game()
app.mainloop()
