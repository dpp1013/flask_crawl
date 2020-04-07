class Queue:
    def __init__(self):
        self.Que = []

    def enter(self, q):
        self.Que.append(q)

    def fetch(self):
        return self.Que.pop(0)

    def empty(self):
        return len(self.Que) == 0
