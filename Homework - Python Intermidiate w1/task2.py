import math
# Создать класс Point2D. Координаты точки задаются 2 параметрами - координатами x, y на плоскости.
class Point2D:
    # Создать защищенный атрибут класса - счетчик созданных экземпляров класса.
    __counter = 0

    # Чтение количества экземпляров реализовать через метод getter.
    @classmethod
    def getter(cls):
        return cls.__counter

    def __init__(self, x, y):
        Point2D.__counter += 1
        self.x = x
        self.y = y

    # Реализовать метод distance который принимает экземпляр класса Point2D и рассчитывает расстояние между 2мя точками на плоскости.
    def distance(self, point):
        return (math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2))

# Создать класс Point3D, который является наследником класса Point2D. Координаты точки задаются 3 параметрами - координатами x, y, z в пространстве.
class Point3D(Point2D):

    def __init__(self, x, y, z):
        super().__init__(x, y)  # Переопределить конструктор с помощью super().
        self.z = z

    def distance(self, point):
        return (math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2 + (point.z - self.z) ** 2))


