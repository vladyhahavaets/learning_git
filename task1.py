class House:

    def __init__(self, temp):
        self.temp = temp

    def heat(self):
        self.temp += 5

    def cond(self):
        self.temp -= 5

