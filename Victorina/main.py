import tkinter
import random
import sys
from tkinter import messagebox

# TODO: Вопросы

ball = 0
answer_count = -1
answer_was = []

questions = {'easy':
                 {'q_1': ['Сколько пешек у одного игрока в шахматах?', '4 пешки', '8 пешек', '10 пешек', '16 пешек', 2],
                  'q_2': ['Самое большое млекопитающее в мире?', 'Слон', 'Лошадь', 'Кит', 'Медведь', 3],
                  'q_3': ['Сколько планет в солнечной системе?', '7 планет', '8 планет', '9 планет', '10 планет', 2],
                  'q_4': ['Какая наука изучает растения?', 'Астрономя', 'Цитология', 'Зоология', 'Ботаника', 4],
                  'q_5': ['Сколько времени рыбачил старик из сказки о Золотой рыбке?', '33 года', '33 месяца',
                          '43 года', '43 месяца', 1],
                  'q_6': ['Самый большой кот на планете, это кот породы...', 'Британский', 'Мэйн-кун', 'Чито', 'Тигр',
                          4],
                  'q_7': ['Единственное млекопитающее, которое умеет летать, это...', 'Летучая мышь', 'Пингвин',
                          'Аэротитан', 'Тапежара', 1],
                  'q_8': ['У каких пород котов нет шерсти?', 'Сиамская', 'Шантильи-тиффани', 'Сфинкс', 'Саванна', 3],
                  'q_9': ['Имя какого волшебника нельзя называть?', 'Волен-Де-Морт', 'Баба-Яга', 'Бастинда',
                          'Снежная Королева', 1],
                  'q_10': ['На каждый Новый Год по традиции пересматривают фильм', 'Чарли и шоколадная фабрика',
                           'Один дома', 'Аватар', 'Полярный Экспресс', 2],
                  'q_11': ['Какое самое медленное животное в мире?', 'Черепаха', 'Змея', 'Ленивец', 'Хамелеон', 3],
                  'q_12': ['Какой самый глубокий океан?', 'Атлантический', 'Индийский', 'Северный ледовитый', 'Тихий',
                           4]
                  },
             'normal':
                 {'q_1': ['Кто открыл электричевство?', 'Бенджамин Франклин', 'Джеёмс Масквелл', 'Никола Тесла',
                          'Галилео Галилей', 1],
                  'q_2': ['В каой стране находится самый высокий водопад Европы?', 'Норвегия', 'Исландия', 'Швеция',
                          'Финляндия', 1],
                  'q_3': ['Как называется самая длинная горная цепь в Южной Америке?', 'Анды', 'Альфы', 'Пампа',
                          'Евразийская степь', 1],
                  'q_4': ['23+(2+10)*2', '70', '45', '58', '47', 4],
                  'q_5': ['Как зовут трёхглавую собаку Хагрида, охраняющую камень в Гарри Поттере?', 'Добби',
                          'Пушистый', 'Горыныч', 'Музыкант', 2],
                  'q_6': ['Какой знак зодака относится к 1 апреля?', 'Водолей', 'Овен', 'Стрелец', 'Рыбы', 2],
                  'q_7': ['У какого химического элемнта наибольшая электроотрицательнось?', 'У кислорода(О)',
                          'У фтора(F)', 'У золота(Au)', 'У гелия(He)', 2],
                  'q_8': ['Крупнейший производитель кофе мира это...', 'Вьетнам', 'Колумбия', 'Индонезия', 'Бразилия',
                          4],
                  'q_9': ['Какой из известных композмтров был глухим?', 'Бах', 'Моцарт', 'Бетховин', 'Гендель', 3],
                  'q_10': ['В каком году Плутоний стал официально \nсчитаться карликовой планетой', '2001', '2004',
                           '2006', '2008', 3],
                  'q_11': ['Солнце состоит из водорода(H) на...', '81%', '90%', '92%', '98%', 3],
                  'q_12': ['Сколько полевых игроков в команде по американскому футболу?', '8 игроков', '9 игроков',
                           '10 игроков', '11 игроков', 4]
                  },
             'diff':
                 {'q_1': ['Дебют в шахматах, начинающиеся ходами королевской пешки из е4 в е6', 'Францущская защита',
                          'Коготь бобра', 'Скандинавская защита', 'Дебют Нимцовича', 1],
                  'q_2': ['Какой термометр появился первым?', 'Жидкостный', 'Механический', 'Оптический', 'Химический',
                          1],
                  'q_3': ['Сколько звёзд в созвездии Малой Медведицы?', '7', '6', '5', '4', 1],
                  'q_4': ['Эту династию в 614 году основал Ли Юань ', 'Цын', 'Тан', 'Цинь', 'Кан', 2],
                  'q_5': [
                      '"Сила тока в проводнике(участке цепи) прямо пропорциональна приложенному напряжению \n и обратно пропорциональна сопротивлению проводника" это закон...',
                      'Ньютога', 'Ома', 'Ампера', 'Паскаля', 2],
                  'q_6': ['Первые три цифры в номере телефона называются...', 'Код страны', 'Код региона',
                          'Код оператора', 'Код телефона', 2],
                  'q_7': [
                      'Как называется фаза игры в покере, когда раздаётся первые три карты\n и как называется фаза, когда ложат 5 открытую карту',
                      'Префлоп и флоп', 'Префлоп и ривер', 'Флоп и ривер', 'Флоп и блайнд', 3],
                  'q_8': ['Белорусское слово "Глеба" переводится как...', 'Яма', 'Ножка стола', 'Почва', 'Гантель', 3],
                  'q_9': [
                      'Чему равна сумма числа пи(n) и Коэффициент ускорения свободного падения(g), \nесли они оба округлены до сотых?',
                      '13,06', '13,96', '12,94', '12,88', 3],
                  'q_10': ['Какая логическая операция возращает истину только \nесли ровно один из операндов равен истине', 'И', 'Или', 'Исключительное И', 'Исключительное Или', 4],
                  'q_11': ['Какая карточная игра играется только одним игроком', 'Дурак', 'Покер', 'Бычки и коровы', 'Пасьянс', 4],
                  'q_12': ['Когда появился СССР?', '4 июля 1943 года', '18 февраля 1923 года', '20 сентября 1932 года', '30 декабря 1922 года', 4],
                  }
             }


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

    def main_question_easy(self):

        global ball, questions, answer_count, answer_was

        questions_easy = [questions['easy']['q_1'], questions['easy']['q_2'], questions['easy']['q_3'],
                          questions['easy']['q_4'], questions['easy']['q_5'], questions['easy']['q_6'],
                          questions['easy']['q_7'], questions['easy']['q_8'], questions['easy']['q_9'],
                          questions['easy']['q_10'], questions['easy']['q_11'], questions['easy']['q_12']
                          ]
        question_easy = random.choice(questions_easy)
        root_quest = tkinter.Label(self, text=question_easy[0], font=('Arial', 10))
        root_quest.place(x=5, y=5)

        # TODO: Лёгкие вопросы

        # 1
        if question_easy == questions['easy']['q_1']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_1'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False, 0, ))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_1'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, True))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_1'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_1'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False, ))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_1'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)


        # 2
        elif question_easy == questions['easy']['q_2']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_1'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_2'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_2'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, True))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_2'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_2'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)


        # 3
        elif question_easy == questions['easy']['q_3']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_3'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_2'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, True))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_3'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_3'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_3'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)


        # 4
        elif question_easy == questions['easy']['q_4']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_4'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_4'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_4'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_4'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, True))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_4'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 5
        elif question_easy == questions['easy']['q_5']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_5'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, True))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_5'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_5'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_5'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_5'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 6
        elif question_easy == questions['easy']['q_6']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_6'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_6'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_6'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_6'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, True))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_6'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 7
        elif question_easy == questions['easy']['q_7']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_7'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, True))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_7'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_7'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_7'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_7'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 8
        elif question_easy == questions['easy']['q_8']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_8'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_8'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_8'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, True))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_8'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_8'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 9
        elif question_easy == questions['easy']['q_9']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_9'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, True))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_9'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_9'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_9'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_9'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 10
        elif question_easy == questions['easy']['q_10']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_10'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_10'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, True))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_10'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_10'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_10'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 11
        elif question_easy == questions['easy']['q_11']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_11'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_11'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_11'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, True))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_11'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_11'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

        # 12
        elif question_easy == questions['easy']['q_12']:

            if question_easy in answer_was:
                questions_easy.remove(questions['easy']['q_12'])
                answer_count -= 1
                self.clear_all(1, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(1, False))
                root_v_1.place(x=80, y=30)
                root_v_1 = tkinter.Label(self, text=questions['easy']['q_12'][1], font=('Arial', 12))
                root_v_1.place(x=160, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(1, False))
                root_v_2.place(x=80, y=70)
                root_v_2 = tkinter.Label(self, text=questions['easy']['q_12'][2], font=('Arial', 12))
                root_v_2.place(x=160, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(1, False))
                root_v_3.place(x=80, y=110)
                root_v_3 = tkinter.Label(self, text=questions['easy']['q_12'][3], font=('Arial', 12))
                root_v_3.place(x=160, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, True))
                root_v_4.place(x=80, y=150)
                root_v_4 = tkinter.Label(self, text=questions['easy']['q_12'][4], font=('Arial', 12))
                root_v_4.place(x=160, y=154)

                answer_was.append(question_easy)

    def main_question_normal(self):
        # TODO: Обычные вопросы

        global ball, questions, answer_count, answer_was

        questions_normal = [questions['normal']['q_1'], questions['normal']['q_2'], questions['normal']['q_3'],
                            questions['normal']['q_4'], questions['normal']['q_5'], questions['normal']['q_6'],
                            questions['normal']['q_7'], questions['normal']['q_8'], questions['normal']['q_9'],
                            questions['normal']['q_10'], questions['normal']['q_11'], questions['normal']['q_12']
                            ]
        question_normal = random.choice(questions_normal)
        root_quest = tkinter.Label(self, text=question_normal[0], font=('Arial', 10))
        root_quest.place(x=5, y=5)

        if question_normal == questions['normal']['q_1']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                        command=lambda: self.clear_all(2, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_3'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                        command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_3'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                        command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_3'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                        command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_3'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_2']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_2'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_2'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_2'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_2'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_3']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_1'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_1'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_1'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_1'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_4']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_4'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_4'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_4'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_4'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_5']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_5'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_5'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_5'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_5'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_6']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_6'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_6'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_6'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_6'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_7']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_7'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_7'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_7'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_7'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_8']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_8'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_8'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_8'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_8'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_9']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_9'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_9'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_9'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_9'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_10']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_10'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_10'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_10'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_10'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)


        elif question_normal == questions['normal']['q_11']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_11'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_11'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_11'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_11'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)




        elif question_normal == questions['normal']['q_12']:

            if question_normal in answer_was:
                answer_count -= 1
                self.clear_all(2, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(2, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['normal']['q_12'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(2, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['normal']['q_12'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(2, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['normal']['q_12'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(2, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['normal']['q_12'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_normal)

    def main_question_diff(self):

        # TODO Сложные вопросы

        global ball, questions, answer_count, answer_was

        questions_diff = [questions['diff']['q_1'], questions['diff']['q_2'], questions['diff']['q_3'],
                            questions['diff']['q_4'], questions['diff']['q_5'], questions['diff']['q_6'],
                            questions['diff']['q_7'], questions['diff']['q_8'], questions['diff']['q_9'],
                            questions['diff']['q_10'], questions['diff']['q_11'], questions['diff']['q_12']
                            ]
        question_diff = random.choice(questions_diff)
        root_quest = tkinter.Label(self, text=question_diff[0], font=('Arial', 10))
        root_quest.place(x=5, y=5)

        if question_diff == questions['diff']['q_1']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_1'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_1'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_1'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_1'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_1'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_2']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_2'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_2'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_2'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_2'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_2'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_3']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_3'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, True))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_3'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_3'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_3'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_3'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_4']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_4'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_4'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_4'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_4'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_4'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_5']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_5'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_5'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_5'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_5'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_5'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_6']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_6'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_6'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_6'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_6'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_6'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_7']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_7'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_7'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_7'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_7'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(1, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_7'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_8']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_8'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_8'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_8'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_8'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_8'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_9']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_9'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_9'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_9'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, True))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_9'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, False, ))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_9'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_10']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_10'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_10'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_10'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_10'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_10'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_11']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_11'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_11'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, False))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_11'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_11'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_11'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)


        elif question_diff == questions['diff']['q_12']:

            if question_diff in answer_was:
                questions_diff.remove(questions['diff']['q_12'])
                answer_count -= 1
                self.clear_all(3, 2)

            else:

                root_v_1 = tkinter.Button(self, text=1, font=('Arial', 12), width=2, height=1, background='red',
                                          command=lambda: self.clear_all(3, False))
                root_v_1.place(x=60, y=30)
                root_v_1 = tkinter.Label(self, text=questions['diff']['q_12'][1], font=('Arial', 12))
                root_v_1.place(x=120, y=34)

                root_v_2 = tkinter.Button(self, text=2, font=('Arial', 12), width=2, height=1, background='yellow',
                                          command=lambda: self.clear_all(3, True))
                root_v_2.place(x=60, y=70)
                root_v_2 = tkinter.Label(self, text=questions['diff']['q_12'][2], font=('Arial', 12))
                root_v_2.place(x=120, y=74)

                root_v_3 = tkinter.Button(self, text=3, font=('Arial', 12), width=2, height=1, background='blue',
                                          command=lambda: self.clear_all(3, False))
                root_v_3.place(x=60, y=110)
                root_v_3 = tkinter.Label(self, text=questions['diff']['q_12'][3], font=('Arial', 12))
                root_v_3.place(x=120, y=114)

                root_v_4 = tkinter.Button(self, text=4, font=('Arial', 12), width=2, height=1, background='green',
                                          command=lambda: self.clear_all(3, True))
                root_v_4.place(x=60, y=150)
                root_v_4 = tkinter.Label(self, text=questions['diff']['q_12'][4], font=('Arial', 12))
                root_v_4.place(x=120, y=154)

                answer_was.append(question_diff)

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
                    self.main_question_easy()
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                    self.main_question_easy()
                else:
                    self.otvet_on_quest(-1)
                    self.main_question_easy()

            elif mod_g == 2:
                if mod_ot:
                    self.otvet_on_quest(2)
                    self.main_question_normal()
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                    self.main_question_easy()
                else:
                    self.otvet_on_quest(-1)
                    self.main_question_normal()

            elif mod_g == 3:
                if mod_ot:
                    self.otvet_on_quest(3)
                    self.main_question_diff()
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                    self.main_question_diff()
                else:
                    self.otvet_on_quest(-1)
                    self.main_question_diff()


            elif mod_g == 4:
                if mod_ot:
                    self.otvet_on_quest(4)
                elif mod_ot == 2:
                    self.otvet_on_quest(0)
                    self.main_question_easy()
                else:
                    self.otvet_on_quest(-1)

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
