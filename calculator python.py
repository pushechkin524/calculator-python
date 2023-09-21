import math

def function_name(tuijy):
    while True:
        try: return float (input(tuijy))
        except ValueError: print("Попробуй еще раз. Число введено неправильно")

def calculator():
    while True:
        try:
            print("Выберите операцию:")
            print("1 Сложение")
            print("2 Вычитание")
            print("3 Умножение")
            print("4 Деление")
            print("5 Возведение в степень n")
            print("6 Квадратный корень")
            print("7 Факториал")
            print("8 Синус")
            print("9 Косинус")
            print("10 Тангенс")
            print("11 Выход из программы")

            operation = float(input("Введите номер операции: "))
            match operation:
                case 1:
                    first = function_name('Введите первое число: \n')
                    second = function_name('Введите второе число: \n')
                    print(f"Ответ: {first + second}\n")
                case 2:
                    first = function_name('Введите первое число: \n')
                    second = function_name('Введите второе число: \n')
                    print(f"Ответ: {first - second}\n")
                case 3:
                    first = function_name('Введите первое число: \n')
                    second = function_name('Введите второе число: \n')
                    print(f"Ответ: {first * second}\n")
                case 4:
                    first = function_name('Введите первое число: \n')
                    second = function_name('Введите второе число: \n')
                    if second != 0:
                        print(f"Ответ: {first / second} \n")
                    else:
                        print(f"На нуль делить нельзя \n")
                case 5:
                    first = function_name('Введите первое число: \n')
                    second = function_name('Введите второе число: \n')
                    print(f"Ответ: {math.pow(first, second)} \n")
                case 6:
                    first = function_name('Введите число: \n')
                    print(f"Ответ: {math.sqrt(first)} \n")
                case 7:
                    first = function_name('Введите число: \n')
                    if first < 0:
                        print("Необходимо ввести целое положительное число")
                    else:
                        print(f"Ответ: {math.factorial(int(first))} \n")
                case 8:
                    first = function_name('Введите число: \n')
                    print(f"Ответ: {math.sin(math.radians(first))} \n")
                case 9:
                    first = function_name('Введите число: \n')
                    print(f"Ответ: {math.cos(math.radians(first))} \n")
                case 10:
                    first = function_name('Введите число: \n')
                    print(f"Ответ: {math.tan(math.radians(first))} \n")
                case 11:
                    exit()
        except ValueError: print(f"\nНеизвестная команда")

calculator()
