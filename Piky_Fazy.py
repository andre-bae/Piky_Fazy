from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random

repeat = 0
repeat1 = 1
num = 5
skolko = 0

# --------------------Start Window--------------------------------------------

start_window = Tk()
# start_window.iconbitmap(default="cow.ico")
start_window.title("Быки и коровы")
start_window.resizable(False, False)
start_window.attributes("-toolwindow", True)
start_window.geometry("500x350+50+100")

instruction = ttk.Label(start_window, text=f'Это игра «Пики и фазы» («Быки и коровы»).\n'
                                           'Требуется угадать случайное число.\n'
                                           'Вводятся пробные цифры.\n' \
                                           'Если цифра по значению и позиции совпала с цифрой в исходном числе,\n'
                                           'то эта цифра – «пика» («бык»).\n'
                                           'Если же цифра не совпала по позиции с цифрой в исходном числе,\n'
                                           'то эта цифра – «фаза» («корова»).\n'
                                           'Например, загадано 1294, а названо 1429. То это 1 «пика» и 3 «фазы»\n'
                                           'А если загадано 02444, а названо 04678. Это 1 «пика» и 1 «фаза», а не 3',
                        font=('Helvetica 10 bold italic'), padding=8)
instruction.pack()

f1 = Frame(start_window, width=500, height=50, borderwidth=1, relief=SOLID)
f1.pack(anchor=NW, padx=5)
f2 = Frame(start_window, width=500, height=50, borderwidth=1, relief=SOLID)
f2.pack(anchor=NW)
f3 = Frame(start_window, width=500, height=50, borderwidth=1, relief=SOLID)
f3.pack(anchor=NW)


def selected(event):
    global num
    num = int(cb_kol.get())


digits = [3, 4, 5, 6]
dg = StringVar(value=digits[2])
label_kol = ttk.Label(f1, text='Количество цифр', font=("Arial", 14))
label_kol.pack(side=LEFT, padx=5, pady=5)
cb_kol = ttk.Combobox(f1, textvariable=dg, font=("Arial", 14), values=digits,
                      state="readonly", width=3, height=4)
cb_kol.pack(side=LEFT, padx=5, pady=5)
cb_kol.bind("<<ComboboxSelected>>", selected)


def checkbutton1_changed():
    global repeat
    repeat = enabled1.get()


enabled1 = IntVar()
label_cb1 = ttk.Label(f2, text="В загаданном числе\nцифры могут повторяться", font=("Arial", 14))
label_cb1.pack(padx=5, pady=5, side=LEFT)
enabled_checkbutton1 = ttk.Checkbutton(f2, variable=enabled1, offvalue=0, onvalue=1,
                                       command=checkbutton1_changed)
enabled_checkbutton1.pack(padx=6, pady=6, side=LEFT)


def checkbutton2_changed():
    global repeat1
    repeat1 = enabled2.get()


enabled2 = IntVar(value=1)
label_cb2 = ttk.Label(f3, text="В вводимых числах\nцифры могут повторяться", font=("Arial", 14))
label_cb2.pack(padx=5, pady=5, side=LEFT)
enabled_checkbutton2 = ttk.Checkbutton(f3, variable=enabled2, offvalue=0, onvalue=1,
                                       command=checkbutton2_changed)
enabled_checkbutton2.pack(padx=6, pady=6, side=LEFT)


# -------------------------Main---------------------------------------

def read_popytka():  # Сравнение введенного и загаданного и вывод результата
    global skolko, cb
    popytka = in_combobox(cb)
    if popytka != '':
        f = 0
        p = 0
        pika = [0] * num
        faza = [0] * num
        for i in range(num):  # Подсчет угаданных цифр на своем месте (Быков)
            pika[i] = (popytka[i] == zagadano[i])
        for i in range(num):  # Подсчет угаданных цифр не на своем месте (коров)
            if not pika[i] and not faza[i]:
                zz = zagadano.count(popytka[i])
                pp = popytka.count(popytka[i])
                if popytka.count(popytka[i]) == zagadano.count(popytka[i]):
                    faza[i] = 1
            print(i, pika, faza, zagadano)
            # for j in range(num):
            # if popytka[j] == zagadano[i]:
            # faza[i] = 1
            # print(i,j,pika,faza, zagadano)
            f += faza[i]  # Всего "быков" и "коров" в попытке
            p += pika[i]
        skolko += 1  # Количество сделанных попыток
        text_rezult.insert(END, f'{skolko} {popytka}: Быков {p}, коров {f}\n')
        if popytka == zagadano:
            text_rezult.insert(END, f'Вы угадали за {skolko} попыток! \nЭто число: {zagadano}\n')


# ----------------------------------------------------------------

def in_combobox(cb):  # Вводим число
    p = ''
    for i, cb in enumerate(comboboxes, start=1):
        tt = cb.get()
        if repeat1 != 1 and tt in p:
            return ''  # Исключаем повторяющеся цифры во вводимом числе
            break
        else:
            p += tt
    return p


# ----------------------------------------------------------------

def game():
    global cb, comboboxes, zagadano, repeat1
    label_kol.pack_forget()
    cb_kol.pack_forget()
    enabled_checkbutton1.pack_forget()
    enabled_checkbutton2.pack_forget()
    btn_start.pack_forget()
    btn_SOS.pack(anchor=NE, padx=(90, 5), pady=5)

    if repeat:  # если в загаданном числе разрешены повторы
        repeat1 = repeat  # то и при вводе их нужно разрешать

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    comboboxes = []
    for i in range(1, num + 1):
        cb = ttk.Combobox(f1, values=digits, font=("Arial", 14),
                          state="readonly", width=3, height=10)
        cb.pack(side=LEFT, padx=5, pady=5)
        cb.current(0)
        comboboxes.append(cb)
    b = Button(f1, text="Ввод", bg="#A9A9A9", width=10,
               font=("Arial", 14), command=read_popytka)
    b.pack(side=LEFT, padx=(15, 5), pady=(5, 15))
    if repeat:
        label_cb1['text'] = "В загаданном числе\nцифры могут повторяться"
    else:
        label_cb1['text'] = "В загаданном числе\nцифры не могут повторяться"
    if repeat1:
        label_cb2['text'] = "В вводимых числах\nцифры могут повторяться"
    else:
        label_cb2['text'] = "В вводимых числах\nцифры не могут повторяться"

    zagadano = str(random.randint(0, 9))  # Загадываем заданное число цифр
    for i in range(1, num):
        fig = str(random.randint(0, 9))
        if repeat != 1:
            while fig in zagadano:  # Исключаем повторяющеся цифры в загаданном числе
                fig = str(random.randint(0, 9))
        zagadano += fig
    print(f'Загадано: {zagadano}')
    zagadano = '40933'


# ----------------------------------------------------------------

def finish_start():
    start_window.destroy()
    log_window.destroy()


def sos():
    text_rezult.insert(END, f'Вы сделали {skolko} попыток.\nА загадано было: {zagadano}\n')
    start_window.destroy()


# ----------------------------------------------------------------

label_povtor = ttk.Label(f3, text="", font=("Arial", 14))
label_povtor.pack(padx=5, pady=5, side=LEFT)

btn_start = Button(f1, text="Играть", bg="#A9A9A9", width=10,
                   font=("Arial", 14), command=game)
btn_start.pack(anchor=NE, padx=(70, 5), pady=5)

btn_SOS = Button(f2, text="Сдаюсь", bg="#A9A9A9", width=10,
                 font=("Arial", 14), command=sos)

btn_fihish = Button(f3, text="Закончить", bg="#A9A9A9", width=10,
                    font=("Arial", 14), command=finish_start)
btn_fihish.pack(anchor=NE, padx=(100, 5), pady=5)

# -------------------------Log Window---------------------------------------

log_window = Tk()
log_window.title("Протокол")
log_window.resizable(False, False)
log_window.attributes("-toolwindow", True)
log_window.geometry("300x400+600+20")

text_rezult = ScrolledText(log_window, width=30, bg="white", wrap=WORD)
text_rezult.pack(padx=(10, 10), side=RIGHT)

log_window.mainloop()
start_window.mainloop()
