from tkinter import *

def print_hello(event):
    print('Hello!')
    print(dir(event))

def init_main_window():
    """
    Инициализация главного окна: создание необходимых виджетов и их упаковка
    :return:
    """
    global root,button1,label,text,scale

    root = Tk()
    button1 = Button(root,text="Привет")
    button1.bind("<Button-1>",print_hello)
    button1.pack()

    variable = IntVar(0)
    label = Label(root,textvariable=variable)
    scale = Scale(root, orient=HORIZONTAL, length=300,
                  from_=0, to=100, tickinterval=20, resolution=5,
                  variable=variable)
    text = Entry(root,textvariable = variable)

    for obj in button1, label, scale, text:
        obj.pack()

if __name__ == "__main__":
    init_main_window()
    root.mainloop()