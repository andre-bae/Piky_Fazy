from tkinter import *
from tkinter import ttk
import random

help_window = Tk()
help_window.title("Описание игры")
# help_window.resizable(False, False)
help_window.attributes("-toolwindow", True)

instruction = ttk.Label(help_window, text=f'Это игра «Пики и фазы» («Быки и коровы»).\n'
                                          'Требуется угадать случайное четырехзначное число.\n'
                                          'Вводятся пробные цифры.\n' \
                                          'Если цифра по значению и позиции совпала с цифрой в исходном числе,\n'
                                          'то эта цифра – «пика» («корова»).\n'
                                          'Если же цифра не совпала по позиции с цифрой в исходном числе,\n'
                                          'то эта цифра – «фаза» («бык»).\n'
                                          'Например, если загадано число 1294, а названо число 1429,\n'
                                          'то это одна «пика» и три «фазы»',
                        font=('Helvetica 12 bold italic'),
                        background='yellow', foreground='brown', padding=8)
instruction.pack()
# ----------------------------------------------------------------

position = {"padx": 6, "pady": 6, "anchor": NW}
easy = "самый легкий. загадывается 5 не повторяющихся цифр"
middle = "Средний. Загадывается от 3 до 6 не повторяющихся цифр"
hard = "Сложный. Загадывается от 3 до 6 цифр, которые могут повторяться"

slogn = IntVar(value=0)  # по умолчанию будет выбран элемент с value=0
slognost = 0


def select_slognost():
    global slognost
    slognost = slogn.get()


#    print(slognost)

header = ttk.Label(help_window, text='Введите уровень сложности игры')
header.pack(**position)

easy_btn = ttk.Radiobutton(text=easy, value=0,
                           variable=slogn, command=select_slognost)
easy_btn.pack(**position)

middle_btn = ttk.Radiobutton(text=middle, value=1,
                             variable=slogn, command=select_slognost)
middle_btn.pack(**position)

hard_btn = ttk.Radiobutton(text=hard, value=2,
                           variable=slogn, command=select_slognost)
hard_btn.pack(**position)


def finish_help():
    help_window.destroy()  # ручное закрытие окна и всего приложения


#    print("Закрытие приложения")

help_window.protocol("WM_DELETE_WINDOW", finish_help)

help_window.mainloop()
# ----------------------------------------------------------------

if slognost != 0:
    digits_window = Tk()
    digits_window.title("Выбор числа загаданных цифр")
    digits_window.resizable(False, False)
    digits_window.attributes("-toolwindow", True)
    #    digits_window.geometry("250x200+400+200")

    position = {"padx": 6, "pady": 6, "anchor": NE}
    digits = [3, 4, 5, 6]
    selected_digit = IntVar(value=5)  # по умолчанию ничего не выборанно
    num = 5
    header = ttk.Label(digits_window, text="Сколько цифр будем отгадывать?")
    header.pack(**position)


    def finish_digits():
        digits_window.destroy()  # ручное закрытие окна и всего приложения


    #        print("Закрытие приложения")

    def select_digits():
        global num
        num = selected_digit.get()


    #        print(slognost, num)

    for dig in digits:
        dig_btn = ttk.Radiobutton(text=dig, value=dig,
                                  variable=selected_digit, command=select_digits)
        dig_btn.pack(**position)

    digits_window.protocol("WM_DELETE_WINDOW", finish_digits)

    digits_window.mainloop()
else:
    num = 5
# ----------------------------------------------------------------
print(slognost, num)
'''
print(f'Это игра «Пики и фазы» («Быки и коровы»).\n' 
      'Требуется угадать случайное четырехзначное число.\n'
      'Вводятся пробные цифры.\n'\
      'Если цифра по значению и позиции совпала с цифрой в исходном числе,\n'
      'то эта цифра – «пика» («корова»).\n'
      'Если же цифра не совпала по позиции с цифрой в исходном числе,\n'
      'то эта цифра – «фаза» («бык»).\n'
      'Например, если загадано число 1294, а названо число 1429,\n'
      'то это одна «пика» и три «фазы»')
print(f'\nВведите уровень сложности игры\n'
      '0 - самый легкий. загадывается 5 цифр и они не повторяются в исходном числе\n'
      '1 - Средний. Загадывается от 3 до 6 не повторяющихся цифр\n'
      '2 - Сложный. Загадывается от 3 до 6 цифр, которые могут повторяться\n'
      '( чем меньше цифр в загаданном числе - тем сложнее игра.\n')
slognost = 3
while slognost > 2:
    N = input('Введите уровень сложности (от 0 до 2)?' )
    if len(N)!=1 or not N.isdigit():        #Если введена не цифра от 0 до 9
        N = input('Введите уровень сложности (от 0 до 2)?' )
    slognost= int(N)

num = 0                                     #Количество загаданных цифр
if slognost==0:
    num = 5
else:
    while num<3 or num>6:
        N = input('сколько цифр будем отгадывать (от 3 до 6)?')
        if len(N)!=1 or not N.isdigit():    #Если введена не цифра от 0 до 9
            N = input('сколько цифр будем отгадывать (от 3 до 6)? ')
        num = int(N)
zagadano = str(random.randint(0,9))         #Загадываем заданное число цифр   
for i in range(1,num):
    fig = str(random.randint(0,9))
    if slognost != 2:
        while fig in zagadano:              #Исключаем повторяющеся цифры
            fig = str(random.randint(0,9))
    zagadano += fig
#    print(zagadano)

#zagadano='02763'
skolko = 0
while True:                           
    f = 0
    p = 0
    pika = [0]*num
    faza = [0]*num
    popytka = input(f'Введите {num} цифр ')

    if popytka=='':                         #завершение игры - ввод пустой строки
        print(f'Жаль! Всего {skolko} попыток! Было загадано {zagadano}')
        break
    while len(popytka)!=num or not popytka.isdigit():  #Если введено не num цифр
        popytka = input(f'Введите {num} цифр ')
    for i in range(num):                    #Подсчет угаданных цифр на своем месте (Быков)
        pika[i] = (popytka[i]==zagadano[i])
    for i in range(num):                    #Подсчет угаданных цифр не на своем месте (коров)
        if not pika[i]:
            for j in range(num):
                faza[i] += (not pika[j]) and (popytka[j]==zagadano[i])
#               print(i,j,pika,faza)
        if faza[i]:                         # Всего "быков" и "коров" в попытке
            faza[i] = 1
        f += faza[i]
        p += pika[i]
    print(f'Быков {p}, коров {f}')
    skolko += 1                             # Количество сделанных попыток
    if popytka==zagadano:
        print(f'Вы угадали за {skolko} попыток! Это {zagadano}')
        break
'''
# okno.mainloop()
# help.mainloop()
