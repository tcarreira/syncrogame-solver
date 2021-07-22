class SyncroGame:
    def __init__(self, level, max_iter, state, _state=None, history=[]):
        self.level = level
        self.max_iter = max_iter
        self.history = history
        self.state = _state if _state else state

    def __str__(self) -> str:
        return f"state={self.state}, history={str(self.history)}"

    def clone(self):
        new = type(self)(_state=self.state, history=[x for x in self.history])
        return new

    def check(self):
        return max(self.state) == len(self.state)

    def square(self):
        if len(self.history) < self.max_iter:
            self.history.append("□")

    def circle(self):
        if len(self.history) < self.max_iter:
            self.history.append("O")

    def triangle(self):
        if len(self.history) < self.max_iter:
            self.history.append("△")


class Level_0(SyncroGame):
    def __init__(self):
        super().__init__(level=0, max_iter=1, state=[1, 1])

    def square(self):
        self.state = [0, 2]
        super().square()
