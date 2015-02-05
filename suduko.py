__author__ = 'garvit'

class sudoko:

    def __init__(self, n):
        if n < 1:
            raise Exception("Number cannot be less that 1");
        self.n = n

    def fillSuduko(self):
        for i in range(self.n):
            input(str(i + 1) + " ")