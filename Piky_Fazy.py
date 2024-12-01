from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import random

repeat = 0
num = 5

# --------------------Start Window--------------------------------------------
start_window = Tk()
start_window.title("Описание игры")
start_window.resizable(False, False)
start_window.attributes("-toolwindow", True)
start_window.geometry("500x240+50+100")

instruction = ttk.Label(start_window, text=f'Это игра «Пики и фазы» («Быки и коровы»).\n'
                                           'Требуется угадать случайное число.\n'
                                           'Вводятся пробные цифры.\n' \
                                           'Если цифра по значению и позиции совпала с цифрой в исходном числе,\n'
                                           'то эта цифра – «пика» («корова»).\n'
                                           'Если же цифра не совпала по позиции с цифрой в исходном числе,\n'
                                           'то эта цифра – «фаза» («бык»).\n'
                                           'Например, если загадано число 1294, а названо число 1429,\n'
                                           'то это одна «пика» и три «фазы»',
                        font=('Helvetica 10 bold italic'),
                        background='yellow', foreground='brown', padding=8)
instruction.pack()

f1 = Frame(start_window, width=50, height=50)
f1.pack(anchor=NW)
f2 = Frame(start_window, width=50, height=50)
f2.pack(anchor=NW)


def selected(event):
    global num
    num = int(combobox.get())


#    print(num, type(num))

digits = [3, 4, 5, 6]
dg = StringVar(value=digits[2])
label = ttk.Label(f1, text='Количество цифр', font=("Arial", 14))
label.pack(side=LEFT, padx=5, pady=5)
combobox = ttk.Combobox(f1, textvariable=dg, font=("Arial", 14), values=digits, state="readonly", width=3, height=2)
combobox.pack(side=LEFT, padx=5, pady=5)
combobox.bind("<<ComboboxSelected>>", selected)


def checkbutton_changed():
    global repeat
    repeat = enabled.get()


#    print(repeat)

enabled = IntVar()
label_cb = ttk.Label(f2, text="Цифры могут повторяться", font=("Arial", 14))
label_cb.pack(padx=5, pady=5, side=LEFT)
enabled_checkbutton = ttk.Checkbutton(f2, variable=enabled, offvalue=0, onvalue=1, command=checkbutton_changed)
enabled_checkbutton.pack(padx=6, pady=6, side=LEFT)


def finish_start():
    start_window.destroy()


btn = Button(start_window, text="Играть", bg="#dbb042", fg="black",
             activebackground="#b58919", activeforeground="black",
             font=("Arial", 14), width=10, height=2, command=finish_start)
btn.place(x=370, y=170)  # pack(anchor=NE, padx=50, pady=10)

start_window.protocol("WM_DELETE_WINDOW", finish_start)
start_window.mainloop()


# -------------------------Main Window---------------------------------------
# print(num, repeat)

def read_popytka():
    global popytka, f, p, pika, faza, skolko, cb
    in_combobox(cb)
    #    popytka = e.get()
    #    e.delete(0,END)
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
                    ff = 0
                    for j in range(num):
                        ff += (not pika[j]) and (popytka[i] == zagadano[j])
                        faza[i] = (ff != 0)
                #                        print(i,j,pika,faza, zagadano)
                #                if faza[i]:                         # Всего "быков" и "коров" в попытке
                #                    faza[i] = 1
                f += faza[i]
                p += pika[i]
            text_rezult.insert(END, f'{popytka}: Быков {p}, коров {f}\n')
            skolko += 1  # Количество сделанных попыток
            if popytka == zagadano:
                text_rezult.insert(END, f'Вы угадали за {skolko} попыток! Это {zagadano}\n')


#                  break
# ----------------------------------------------------------------
zagadano = str(random.randint(0, 9))  # Загадываем заданное число цифр
for i in range(1, num):
    fig = str(random.randint(0, 9))
    if repeat != 1:
        while fig in zagadano:  # Исключаем повторяющеся цифры
            fig = str(random.randint(0, 9))
    zagadano += fig
print(f'Загадано: {zagadano}')
# zagadano='131'
# ----------------------------------------------------------------
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
skolko = 0
f = 0
p = 0
pika = [0] * num
faza = [0] * num
# ----------------------------------------------------------------
main_window = Tk()
main_window.title("Быки и коровы")
# main_window.resizable(False, False)
main_window.attributes("-toolwindow", True)
# main_window.geometry("400x400+400+200")

# frame_ask = Frame(main_window, borderwidth=1, relief=SOLID)
# frame_ask.pack(side=LEFT)
# frame_rezult = Frame(main_window, borderwidth=1, relief=SOLID)
# frame_rezult.pack(side=RIGHT)
comboboxes = []
popytka = ''

for i in range(1, num + 1):
    #    print(i)
    cb = ttk.Combobox(main_window, values=digits, font=("Arial", 14),
                      state="readonly", width=3, height=10)
    cb.pack(side=LEFT, padx=5, pady=5)  # grid(row=0, column=i)
    cb.current(0)
    comboboxes.append(cb)


def in_combobox(cb):
    global popytka
    popytka = ''
    for i, cb in enumerate(comboboxes, start=1):
        tt = cb.get()
        popytka += tt


#    print(popytka)

# def print_values():
#    global popytka
#    for i, cb in enumerate(comboboxes, start=1):
##        tt = cb.get()
##        print(f"Combobox {i}: {tt}")
#        popytka +=cb.get()
#        print(popytka)
# btn = Button(main_window, text="Print Values", command=print_values)
# btn.pack(side=LEFT, padx=5, pady=5)#grid(row=3, column=0)


'''
invite = Label(frame_ask, text=f'Введите {num} цифр', justify="left",
                       bg="white", fg="black", font="Courier 18 bold")
invite.pack(side=TOP)
e = Entry(frame_ask, width=num, justify="left", bg="white", fg="black",
              font="Courier 24 bold")
e.pack(side=LEFT)
'''
b = Button(main_window, text="Ввод", bg="brown",
           font="Courier 12 bold", command=read_popytka)
b.pack(side=LEFT)

# -------------------------Log Window---------------------------------------
log_window = Tk()
log_window.title("Протокол")
# log_window.resizable(False, False)
log_window.attributes("-toolwindow", True)
log_window.geometry("320x400+600+20")
text_rezult = Text(log_window, width=40, height=8, bg="white", wrap=WORD)
text_rezult.pack(side=RIGHT)
text_rezult.grid(column=0, row=0, sticky=NSEW)
# scroll = ttk.Scrollbar(orient = "vertical", command = text_rezult.yview)
# scroll.grid(column = 1, row = 0, sticky = NS)
# scroll = Scrollbar(command=text_rezult.yview)
# scroll.pack(side=LEFT, fill=Y)
# text_rezult.config(yscrollcommand=scroll.set)


log_window.mainloop()
main_window.mainloop()
