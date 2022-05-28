#Необходимо написать функцию калькулятор, которая принимает строку состоящую из числа, оператора и
#второго числа разделенных пробелом. Например ('1 + 1'); Необходимо разделить строку используя str.split(), и
#проверить является результирующий список валидным.
class FormulaError(ValueError):
    pass

def calc():
    str = input("Введите три символа через пробел: ")
    list_str = str.split()
    # a) Если ввод не состоит из 3 элементов, необходимо возбудить исключение FormulaError, которое является
    #пользовательским исключением.
    if len(list_str) != 3:
        raise FormulaError("Количество введенных символов не равняется 3")
    else:
        try:
            # b) Попытайтесь сконвертировать первое и третье значение ввода к типу float.Перехватите любые
            # исключения типа ValueError, которые возникают, и выбросите FormulaError
            list_str[0], list_str[2] = float(list_str[0]), float(list_str[2])
        except ValueError:
            raise FormulaError("Первый или третий символ в строке не возможно преобразовать к типу float")
        # c) Если второе значение ввода не является '+', '-', '*', '/' также выбросите FormulaError
        if list_str[1] not in {'+', '-', '*', '/'}:
            raise FormulaError("Вторым значением в строке должна быть одна из операций '+', '-', '*', '/'")
        # Если инпут валидный - ф-я должна вернуть результат операции
        else:
            if list_str[1] == "+":
                res = list_str[0] + list_str[2]
            elif list_str[1] == "-":
                res = list_str[0] - list_str[2]
            elif list_str[1] == "*":
                res = list_str[0] * list_str[2]
            elif list_str[1] == "/":
                res = list_str[0] / list_str[2]
    return res

print(calc())
