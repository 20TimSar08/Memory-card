#создай приложение для запоминания информации
from PyQt5.QtCore import Qt, QCoreApplication
from random import shuffle, randint
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, new_question, right_answer, wrong_1, wrong_2, wrong_3):
        self.new_question = new_question
        self.right_answer = right_answer
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Английский', 'Испанский'))
questions_list.append(Question('Первая буква в алфавите', 'Аа', 'Бб', 'Вв', 'Гг'))
questions_list.append(Question('Кто выиграл последний чемпионат по CS: GO?', 'NaVi', 'Spirit', 'Liquid', 'Champions'))
questions_list.append(Question('Кто выиграл "Золотой мяч" 2018?', 'Luca Modric', 'Cristiano Ronaldo', 'Leonel Messi', 'Ricardo Kaka'))
questions_list.append(Question('Какая карта существует прямо сейчас в CS: GO?', 'Office', 'Killhouse', 'Mirage 2.0', 'Pitstop'))
questions_list.append(Question('Кто первый высадился на Луне?', 'Нил Армстронг', 'Юрий Гагарин', 'Алексей Леонов', 'Валентина Терешкова'))
questions_list.append(Question('Кто выиграл Чемпионат мира по футболу в 1950 году?', 'Уругвай', 'Венгрия', 'Испания', 'Бразилия'))
questions_list.append(Question('Как будет "Пайтон" по-английски?', 'Python', 'Pyton', 'Piton', 'Pyhton'))
questions_list.append(Question('Какой позиции нет в футболе?', '"Ложная десятка"', 'Правофланговый нападающий', 'Центальный защитник', 'Правый защитник'))
questions_list.append(Question('Какого клуба не существует в профессиональном футболе?', 'Liverpool United', 'Real Zaragosa', 'West Ham United', 'Manchester United'))

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(300, 250)
btn_answer = QPushButton('Ответить') # кнопка ответа
exit_b = QPushButton('Выход')
question = QLabel('Какой национальности не существует?')  # текст вопроса

answers_group = QGroupBox('Варианты ответов') # группа на экране для переключателей с ответами

answer1 = QRadioButton('Энцы')
answer2 = QRadioButton('Смурфы')
answer3 = QRadioButton('Чумыльцы')
answer4 = QRadioButton('Алеуты')
RadioGroup = QButtonGroup()  # это для группировки переключателей, чтобы управлять их поведением

RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

group_vertical1 = QVBoxLayout()
group_vertical2 = QVBoxLayout()
group_horizontal = QHBoxLayout()
group_vertical1.addWidget(answer1)
group_vertical1.addWidget(answer2)
group_vertical2.addWidget(answer3)
group_vertical2.addWidget(answer4)
group_horizontal.addLayout(group_vertical1)
group_horizontal.addLayout(group_vertical2)
answers_group.setLayout(group_horizontal)# готова "панель" с вариантами ответов

correct_aswer_group = QGroupBox('Результат теста')
wrong_right = QLabel('Правильно/Неправильно')
correct_answer = QLabel('Правильный ответ')
correct_answer_vertical = QVBoxLayout()
correct_answer_vertical.addWidget(wrong_right, alignment = Qt.AlignLeft)
correct_answer_vertical.addWidget(correct_answer, alignment = Qt.AlignHCenter)
correct_aswer_group.setLayout(correct_answer_vertical)


question_horizontal = QHBoxLayout()
btn_answer_horizontal = QHBoxLayout()
answers_group_horizontal = QHBoxLayout()

main_vertical = QVBoxLayout()
question_horizontal.addWidget(question, alignment = Qt.AlignHCenter)
btn_answer_horizontal.addWidget(btn_answer, alignment = Qt.AlignHCenter, stretch = 2)
btn_answer_horizontal.addWidget(exit_b, alignment = Qt.AlignRight)
answers_group_horizontal.addWidget(answers_group, alignment = Qt.AlignHCenter)
answers_group_horizontal.addWidget(correct_aswer_group)
correct_aswer_group.hide()

main_vertical.addLayout(question_horizontal)
main_vertical.addLayout(answers_group_horizontal)

main_vertical.addLayout(btn_answer_horizontal)
main_vertical.setSpacing(5)

def show_result():
    answers_group.hide()
    correct_aswer_group.show() 
    btn_answer.setText('Следующий вопрос')


def show_question():
    correct_aswer_group.hide()
    answers_group.show()
    btn_answer.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [answer1, answer2, answer3, answer4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_1)
    answers[2].setText(q.wrong_2)
    answers[3].setText(q.wrong_3)
    question.setText(q.new_question)
    correct_answer.setText(q.right_answer)
    show_question()

def show_correct(result):
    wrong_right.setText(result)
    show_result()

def next_question():
    main_win.total += 1
    print('Статистика\nВсего вопросов:', main_win.total,'\nПравильных ответов:', main_win.score)
    cur_question = randint(0, len(questions_list)-1)
    q = questions_list[cur_question]
    ask(q)
    questions_list.remove(questions_list[cur_question])
    if len(questions_list)==-1:
        show_correct('Вопросы закончились!')


def clck_OK():
    if btn_answer.text()=='Ответить':
        check_answer()
    else:
        next_question()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_win.score += 1
        print('Статистика\nВсего вопросов:', main_win.total,'\nПравильных ответов:', main_win.score)
        print('Рейтинг:', main_win.score/main_win.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')

main_win.cur_question = -1
btn_answer.clicked.connect(clck_OK)
main_win.score = 0
main_win.total = 0
next_question()
main_win.setLayout(main_vertical)
exit_b.clicked.connect(QCoreApplication.instance().quit)
main_win.show()
app.exec_()
