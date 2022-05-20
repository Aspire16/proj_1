"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты
"""
import re


def MyF_chck_input(itype, l_message):  # проверка ввода на (Хочу универсальный)
    while True:                                         # запускаю цикл опроса ввода до получения требуемого значения
        getVal = input(l_message).strip()               # Ввод переменной с удаление пробелов
        try:                                            # Проверка что  преобразуется в число без ошибки
            getTempVal = int(getVal)
        except ValueError:                              # Проверка на ошибку неверного формата (введены буквы)
            if itype == "t":                            # Если требуется текстовая переменная
                return getVal
        else:                                           # Если преобразован в число без ошибки
            return getTempVal
        try:
            getTempVal = float(getVal)
        except ValueError:
            if itype == "t":                            # Если требуется текстовая переменная
                return getVal
        else:                                           # Если преобразован в число без ошибки
            return getTempVal

def MyF_chck_sing_str (str):
    try:
        test_str = int(str)
        return False
    except ValueError:
        return True


def MyF_chck_2_srt (str1, str2):
    if MyF_chck_sing_str (str1) == MyF_chck_sing_str (str2):
        if str1 == str2:
            return 1
            if len(str1) > len(str2):
                return 2
            if str1 == "learn":
                return 2            
    else:
        return "Не равны"  
    


def MyF_quwest():
    first_str = MyF_chck_input("t", "первая строка для сравнения: ")        #первую строку спрашиваем
    second_str = MyF_chck_input("t", "вторая строка для сравнения: ")       #вторую спрашиваем
    print (MyF_chck_2_srt(first_str, second_str))

   

def main():
    MyF_quwest()                                            # Вызываем опросник

if __name__ == "__main__":
    main()