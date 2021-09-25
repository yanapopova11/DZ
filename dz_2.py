while True:
    num_1 = input ("Введите первое число: ")
    z = input ("Введите знак операции (+,-,*,/): ")
    num_2 = input ("Введите второе число: ")
    if num_1.isdigit() == True and num_2.isdigit() == True:
            num_1 = float(num_1)
            num_2 = float(num_2)
    else:
        print("Вы ввели не число, операция не может быть вычислена")
    if z == '+':
        print("Результат: ", num_1 + num_2)
    elif z == '-':
        print( "Результат: ", num_1 - num_2)
    elif z == '*':
        print( "Результат: ", num_1 * num_2)
    elif z == '/':
        if num_2 == 0 :
            print("Деление на ноль невозможно")
        else:
            print("Результат: ", num_1 / num_2)
    else:
        print("Вы ввели знак неподдерживаемой операции")
    stop = input("Для завершения работы введите букву 'q', \nили любую другую, чтобы продолжить : ")
    if stop == 'q':
        print ("Спасибо, что воспользовались нашим калькулятором")
        break

