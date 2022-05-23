"""
Домашнее задание №1
Цикл for: Продажи товаров
* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""



traid_hist =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]


def calk_sold (S_list, type_calk):  # на входе список продаж и тип подсчета среднее или все считаем
    Sold_summ = 0
    for sld in S_list:              # перебираем все зачения и суммируем 
        Sold_summ += sld
    if type_calk == "average":          # если среднее арифметическое то делим на количество и возвращаем
        average_Sold_summ = Sold_summ // len(S_list)
        return average_Sold_summ
    if type_calk == "all":          # если просто сумма то возвращаем ее
        return Sold_summ

def calc_all ():
    average_summ_all_prod = 0
    all_summ_sold_all_prod = 0
    print (f"product average all")
    for C_phone in traid_hist: # перебираем весь список продаж и делаем подсчеты
        average_summ_sold = 0
        all_summ_sold = 0
        average_summ_sold = calk_sold(C_phone["items_sold"], "average") # среднее
        all_summ_sold = calk_sold(C_phone["items_sold"], "all") # общее кол-во
        print (f"{C_phone['product']} {average_summ_sold} {all_summ_sold}" ) # выводим на печать
        average_summ_all_prod += average_summ_sold # суммируем средние продажы
        all_summ_sold_all_prod += all_summ_sold     # суммируем вс епродажы
    print (f"'ITOGO' {average_summ_all_prod} {all_summ_sold_all_prod}" ) # выводим на печать итоги

def main():
    calc_all ()
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
   
    
if __name__ == "__main__":
    main()