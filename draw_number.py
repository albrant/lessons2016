import turtle
#from math import sin
default_size = 10
default_interval = 4


def draw_number(turt, number, size=default_size, interval=default_interval):
    """ черепаха turt выводит на экран нарисованные цифры, входящие в число number.
    Число не может начинаться нулём (используется обычная десятичная запись)
    Вывод происходит в том направлении, в котором стояла черепаха
    начальная точка, в которой была черепаха, - левый нижний угол первой цифры числа.
    После рисования черепаха останется в том же направлении на расстоянии
    interval от правой нижней кромки последней цифры числа"""
    turt.color("darkgreen")
    des = len(str(number))
    L1 = size/2
    L2 = (size/2)*2**0.5
    while des>0:
        digit = number // 10**(des-1) # первая цифра числа
        if digit == 0:
            B = [180, -90,-90,-90]
            A = [ L1,2*L1, L1,2*L1]
            sdvig = L1
        elif digit == 1:
            B = [90,  135]
            A = [2*L1,L2]
            sdvig = L1
        elif digit == 2:
            B = [180, -135, 45, 90]
            A = [ L1,   L2, L1, L1]
            sdvig = L1
        elif digit == 3:
            B = [45, 135,-135,135]
            A = [ L2,  L1,  L2, L1]
            sdvig = 0
        elif digit == 4:
            B = [90, 180,270,-90]
            A = [2*L1,L1, L1, L1]
            sdvig = L1
        elif digit == 5:
            B = [0, 90,90,-90,-90]
            A = [L1,L1,L1, L1, L1]
            sdvig = 0
        elif digit == 6:
            B = [0, 90,90,90,180,-45]
            A = [L1,L1,L1,L1, L1, L2]
            sdvig = 0
        elif digit == 7:
            B = [90,-45,135]
            A = [L1, L2, L1]
            sdvig = 0
        elif digit == 8:
            B = [  90,-90, -90,-90,-90,-90]
            A = [2*L1, L1,2*L1, L1, L1, L1]
            sdvig = 0
        elif digit == 9:
            B = [45,45,90,90,90]
            A = [L2,L1,L1,L1,L1]
            sdvig = 0

        turt.penup()
        turt.forward(sdvig)
        turt.pendown()
        for lenght, degree in zip(A, B):
            turt.left(degree)
            turt.forward(lenght)
        A.reverse()
        B.reverse()
        for lenght, degree in zip(A, B):
            turt.backward(lenght)
            turt.right(degree)
        turt.penup()
        turt.forward(L1-sdvig)#если до начала рисования сдвига не было, он все равно нужен
        number = number % (10**(des-1)) #остаток от числа без первой цифры
        turt.forward(interval) #делаем отступ от предыдущей цифры
        des -=1