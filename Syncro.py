class SyncroGame:
    def __init__(self, level, max_iter, state, history=None, _state=None):
        self.level = level
        self.max_iter = max_iter
        self.history = history if history else []
        self.state = _state if _state else state

    def __str__(self) -> str:
        return f"state={self.state}, history={str(self.history)}"

    def clone(self):
        new = type(self)(_state=self.state, history=[x for x in self.history])
        return new

    def check(self):
        return max(self.state) == len(self.state)

    def __call__(self, move: str):
        if move == "square":
            return self.square()
        elif move == "circle":
            return self.circle()
        elif move == "triangle":
            return self.triangle()
        else:
            raise RuntimeError(f"This move ({move})) is not supported")

    def solve(self):
        solution = self._solve()
        if solution:
            print(f"Level {solution.level}: {solution.history}")
        else:
            print(f"Level {self.level}: FAILED")

    def _solve(self):
        if self.check():
            return self
        if len(self.history) >= self.max_iter:
            return None

        for move in ["square", "circle", "triangle"]:
            next_state = self.clone()
            result = next_state(move)._solve()
            if result:
                return result

    def square(self):
        if len(self.history) < self.max_iter:
            self.history.append("□")
        return self

    def circle(self):
        if len(self.history) < self.max_iter:
            self.history.append("O")
        return self

    def triangle(self):
        if len(self.history) < self.max_iter:
            self.history.append("△")
        return self


class Level_0(SyncroGame):
    def __init__(self, *args, **kwargs):
        super().__init__(level=0, max_iter=1, state=[1, 1], *args, **kwargs)

    def square(self):
        self.state = [0, 2]
        return super().square()


class Level_1(SyncroGame):
    def __init__(self, *args, **kwargs):
        super().__init__(level=1, max_iter=1, state=[1, 1], *args, **kwargs)

    def square(self):
        self.state = [0, 2]
        return super().square()

    def circle(self):
        self.state = [1, 1]
        return super().circle()


class Level_2(SyncroGame):
    def __init__(self, *args, **kwargs):
        super().__init__(level=2, max_iter=2, state=[1, 1, 1], *args, **kwargs)

    def square(self):
        prev = [x for x in self.state]
        self.state = [prev[2], *prev[:2]]
        return super().square()

    def circle(self):
        prev = [x for x in self.state]
        self.state[0] = prev[1]
        self.state[1] = 0
        self.state[2] = prev[2] + prev[0]
        return super().circle()


class Level_3(SyncroGame):
    def __init__(self, *args, **kwargs):
        super().__init__(level=3, max_iter=3, state=[1, 1, 1], *args, **kwargs)

    def square(self):
        prev = [x for x in self.state]
        self.state[0] = prev[2]
        self.state[1] = 0
        self.state[2] = prev[0] + prev[1]
        return super().square()

    def circle(self):
        prev = [x for x in self.state]
        self.state = [prev[2], *prev[:2]]
        return super().circle()


# template
class Level_Z(SyncroGame):
    def __init__(self, *args, **kwargs):
        super().__init__(level=0, max_iter=0,
                         state=[1, 1, 1, 1], *args, **kwargs)

    def square(self):
        prev = [x for x in self.state]

        return super().square()

    def circle(self):
        prev = [x for x in self.state]

        return super().circle()
