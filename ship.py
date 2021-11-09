

class Ship():
    hits = 0

    def __init__(self, r, c, n, direction):
        self.n = n

        if direction == 1: #across
            self.r = [(r + i) for i in range(n)]
            self.c = [c for i in range(n)]
        else: #down
            self.r = [r for i in range(n)]
            self.c = [(c + i) for i in range(n)]

    def print_all(self):
        print(self.r)
        print(self.c)

    def is_hit(self, r, c):
        if r in self.r and c in self.c:
            self.__class__.hits += 1
            return True
        return False

    def is_sunk(self):
        if self.__class__.hits >= n:
            return True
        return False
