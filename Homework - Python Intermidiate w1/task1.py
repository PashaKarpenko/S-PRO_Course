# Добавить класс миксин, в котором реализовать статические методы, для этих же операций(add, sub, mull, div).

class fractionMixin:
    @staticmethod
    def sub(fraction1, fraction2):
        return Fraction(fraction1.num * fraction2.den - fraction1.den * fraction2.num,
                        fraction1.den * fraction2.den)

    @staticmethod
    def add(fraction1, fraction2):
        return Fraction(fraction1.num * fraction2.den + fraction1.den * fraction2.num,
                        fraction1.den * fraction2.den)

    @staticmethod
    def mul(fraction1, fraction2):
        return Fraction(fraction1.num * fraction2.num, fraction1.den * fraction2.den)

    @staticmethod
    def truediv(fraction1, fraction2):
        return Fraction(fraction1.num * fraction2.den, fraction1.den * fraction2.num)

# Создать класс дробь(Fraction), конструктор которого принимает целые числа (num, den - числитель(numerator), знаменатель(denominator) ).
# Добавить класс миксин в класс Fraction

class Fraction(fractionMixin):
    def __init__(self, num, den):
        self.__num = num
        self.__den = den

    # Атрибуты числитель и знаменатель в классе сделать приватными. Доступ к атрибутам реализовать через свойства.

    @property
    def num(self):
        return self.__num

    @property
    def den(self):
        return self.__den

    @num.setter
    def num(self, __num):
        self.__num = num

    @den.setter
    def den(self, __den):
        assert den > 0, 'Знаменатель дроби должен быть больше 0'
        self.__den = den

    # Переопределить методы __sub__, __add__, __mull__, __truediv__
    # для того, чтобы можно было выполнять соответствующие математические действия с объектами класса дробь.
    # (Вычитание, сложение, умножение и деление).

    def __sub__(self, fraction):
        num = self.num * fraction.den - self.den * fraction.num
        den = self.den * fraction.den

        return Fraction(num, den)

    def __add__(self, fraction):
        num = self.num * fraction.den + self.den * fraction.num
        den = self.den * fraction.den

        return Fraction(num, den)

    def __mul__(self, fraction):
        num = self.num * fraction.num
        den = self.den * fraction.den

        return Fraction(num, den)

    def __truediv__(self, fraction):
        num = self.num * fraction.den
        den = self.den * fraction.num

        return Fraction(num, den)

    # Создать classmethod который из строки типа 'числитель/знаменатель'
    # возвращает объект класса дробь.

    @classmethod
    def fraction_from_string(cls, fraction_string):
        num, den = [int(i.strip()) for i in fraction_string.split('/')]
        return cls(num, den)

    # Переопределить метод __str__, который при выводе объекта на печать будет выводить строку вида num / den.

    def __str__(self):
        return f'{self.num}/{self.den}'

# Создать объекты класса дробь.

num = 3
den = 5
fraction_string = '1/2'

fraction1 = Fraction(num, den)
print(f"{fraction1} — переопределенный __str__")

fraction2 = Fraction.fraction_from_string(fraction_string)
print(f"{fraction2} — @classmethod\n")


# Выполнить все реализованные методы.


print(f"{fraction1 - fraction2} — __sub__")
print(f"{fraction1 + fraction2} — __add__")
print(f"{fraction1 * fraction2} — __mul__")
print(f"{fraction1 / fraction2} — __truediv__\n")

print(f"{fraction1.sub(fraction1, fraction2)} — sub")
print(f"{fraction1.add(fraction1, fraction2)} — add")
print(f"{fraction1.mul(fraction1, fraction2)} — mul")
print(f"{fraction1.truediv(fraction1, fraction2)} — truediv")



