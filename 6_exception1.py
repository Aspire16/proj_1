"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def MyF_chck_input(itype, l_message):  # проверка ввода на (Хочу универсальный)
    while True:                                         # запускаю цикл опроса ввода до получения требуемого значения
        getVal = input(l_message).strip()               # Ввод переменной с удаление пробелов
        try:                                            # Проверка что  преобразуется в число без ошибки
            getTempVal = int(getVal)
        except ValueError:                              # Проверка на ошибку неверного формата (введены буквы)
            if itype == "t":                            # Если требуется текстовая переменная
                return getVal
        else:                                           # Если преобразован в число без ошибки
            return getTempVal                  # требуется положительное число
        print ("Ошибка ввода")


def hello_user():
    try:
        while True:
            if MyF_chck_input("t", "Как дела? ") == "Хорошо":
                print ("Это радует")
                return 1
    except KeyboardInterrupt:
        exit("Пока")    

    
if __name__ == "__main__":
    hello_user()