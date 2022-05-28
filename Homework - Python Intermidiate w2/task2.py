# Определите класс итератор ReverseIter, который принимает список и итерируется по нему в обратном направлении
class ReverseIter():
    def __init__(self, r):
        self.r = r

    def __iter__(self):
        self.i = len(self.r)
        return self

    def __next__(self):
        if self.i > 0:
            self.i -= 1
            return self.r[self.i]


        else:
            raise StopIteration


my_number = ReverseIter([0, 1, 2, 3, 4, 5])

for j in my_number:
    print(j)