class Stack:
    def __init__(self):
        self.st = []

    def pop(self):
        return self.st.pop()

    def push(self, s):
        self.st.append(s)

    def empty(self):
        return len(self.st)==0

