def getInput():
    string = input("Введите строку ")
    return string

def testInput(string):
    return string.isdecimal()

def strToInt(string):
    number = int(string)
    return number

def printInt(number):
    print(number)

string = getInput()
if testInput(string) is True:
    number = strToInt(string)
    printInt(number)
else:
    print("Данную строку невозможно преобразовать в целое число.")