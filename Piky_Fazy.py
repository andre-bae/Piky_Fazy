from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
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
                        font='Helvetica 12 bold italic',
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

header = ttk.Label(help_window, text='Введите уровень сложности игры',
                   font='Helvetica 12 bold italic',
                   background='yellow', foreground='brown', padding=8)
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

btn = Button(help_window, text="Click me", bg="#dbb042", fg="black",
             activebackground="#b58919", activeforeground="black",
             font=("Arial", 14), width=15, height=3, command=finish_help)
btn.pack(pady=10)

help_window.protocol("WM_DELETE_WINDOW", finish_help)

help_window.mainloop()
# ----------------------------------------------------------------

if slognost != 0:  # , state=["disabled"]
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

    btn = Button(digits_window, text="Click me", bg="#dbb042", fg="black",
                 activebackground="#b58919", activeforeground="black",
                 font=("Arial", 14), width=15, height=3, command=finish_digits)
    btn.pack(pady=10)

    digits_window.protocol("WM_DELETE_WINDOW", finish_digits)

    digits_window.mainloop()
else:
    num = 5
# ----------------------------------------------------------------
# print(slognost, num)

zagadano = str(random.randint(0, 9))  # Загадываем заданное число цифр
for i in range(1, num):
    fig = str(random.randint(0, 9))
    if slognost != 2:
        while fig in zagadano:  # Исключаем повторяющеся цифры
            fig = str(random.randint(0, 9))
    zagadano += fig
#    print(zagadano)
# zagadano='13074'

skolko = 0
# while True:
f = 0
p = 0
pika = [0] * num
faza = [0] * num
#    popytka = input(f'Введите {num} цифр ')
main_window = Tk()
main_window.title("Быки и коровы")
# main_window.resizable(False, False)
main_window.attributes("-toolwindow", True)
# main_window.geometry("250x200+400+200")

frame_ask = Frame(main_window)
frame_ask.pack(side=LEFT)
frame_rezult = Frame(main_window)
frame_rezult.pack(side=RIGHT)


def read_popytka():
    global popytka, f, p, pika, faza, skolko
    popytka = e.get()
    e.delete(0, END)
    f = 0
    p = 0
    pika = [0] * num
    faza = [0] * num
    if popytka == '':  # завершение игры - ввод пустой строки
        text_rezult.insert(END, f'Жаль! Всего {skolko} попыток! Было загадано {zagadano}\n')
    #            break
    else:
        if len(popytka) == num and popytka.isdigit():  # Если введено не num цифр

            for i in range(num):  # Подсчет угаданных цифр на своем месте (Быков)
                pika[i] = (popytka[i] == zagadano[i])
            for i in range(num):  # Подсчет угаданных цифр не на своем месте (коров)
                if not pika[i]:
                    for j in range(num):
                        faza[i] += (not pika[j]) and (popytka[j] == zagadano[i])
                #                        print(i,j,pika,faza)
                if faza[i]:  # Всего "быков" и "коров" в попытке
                    faza[i] = 1
                f += faza[i]
                p += pika[i]
            text_rezult.insert(END, f'{popytka}: Быков {p}, коров {f}\n')
            skolko += 1  # Количество сделанных попыток
            if popytka == zagadano:
                text_rezult.insert(END, f'Вы угадали за {skolko} попыток! Это {zagadano}\n')


#                  break

invite = Label(frame_ask, text=f'Введите {num} цифр', justify="left",
               bg="white", fg="black", font="Courier 18 bold")
invite.pack(side=TOP)
e = Entry(frame_ask, width=num, justify="left", bg="white", fg="black",
          font="Courier 24 bold")
e.pack(side=LEFT)
b = Button(frame_ask, text="Ввод", bg="brown",
           font="Courier 12 bold", command=read_popytka)
b.pack(side=LEFT)

# text_rezult = Text(frame_rezult, width=40, height=8, bg="white", wrap=WORD)
text_rezult = ScrolledText(frame_rezult, width=40, height=8, bg="white", wrap=WORD)
text_rezult.pack(side=RIGHT)
# text_rezult.grid(column = 0, row = 0, sticky = NSEW)
# scroll = ttk.Scrollbar(orient = "vertical", command = text_rezult.yview)
# scroll.grid(column = 1, row = 0, sticky = NS)
# scroll = Scrollbar(command=text_rezult.yview)
# scroll.pack(side=LEFT, fill=Y)
# text_rezult.config(yscrollcommand=scroll.set)


main_window.mainloop()
