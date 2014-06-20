__author__ = 'Xidai'


class UF:
    def __init__(self, n):
        self.id = []
        for i in range(0, n):
            self.id[i] = i

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        if not self.connected(p, q):
            origin = self.id[p]
            target = self.id[q]
            for i in range(0, len(self.id)):
                if self.id[i] == origin:
                    self.id[i] = target


class QuickUnionUF:
    def __init__(self, n):
        self.id = []
        for i in range(0, n):
            self.id[i] = i

    def root(self, i):
        if self.id[i] == i:
            return i
        else:
            return self.root(self.id[i])

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)
        self.id[root_p] = root_q