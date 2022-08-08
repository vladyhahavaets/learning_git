class House:

    def __init__(self, temp=15):
        self.temp = temp

    def heat(self):
        self.temp += 5

    def cond(self):
        self.temp -= 5

