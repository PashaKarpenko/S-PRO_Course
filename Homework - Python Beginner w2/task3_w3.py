# Напишите программу, в которой вызывается функция, запрашивающая с ввода  две строки
# и возвращающая в программу  результат их конкатенации.

def concatenation(string1 = input("Введите строку "), string2 = input("Введите строку ")):
    return(string1 + string2)
print(concatenation()) # Выведите результат на экран.

# Напишите функцию, которая считывает с клавиатуры числа и перемножает их
# до тех пор, пока не будет введен 0. Функция должна возвращать
# полученное произведение. Вызовите функцию и выведите на экран результат
# ее работы.

def function():
    i = 1
    number = 1
    while number != 0:
        i *= number
        number = int(input("Введите число "))
    return (i)

print(function())


