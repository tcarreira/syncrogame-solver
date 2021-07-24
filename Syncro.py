from typing import Dict, List


class SyncroGame:
    translation = {
        "square": "□",
        "circle": "O",
        "triangle": "△",
    }

    def __init__(
        self, level: int, cardinality: int, max_iter: int, rules: Dict, debug=False
    ):
        self.level = level
        self.max_iter = max_iter
        self.cardinality = cardinality
        self.rules = rules
        self.state = [1] * cardinality
        self.history = []
        self._seen = set()
        self.debug = debug

    def set_state(self, state: List[int]):
        self.state = state
        return self

    def set_history(self, history: List[str]):
        self.history = history
        return self

    def get_history(self) -> List[str]:
        return [self.translation[x] for x in self.history]

    def __repr__(self) -> str:
        return f"(L{self.level}) state={self.state}, history={self.get_history()}"

    def __str__(self) -> str:
        return f"Level {self.level}: {self.get_history()}"

    def check(self, state=None) -> bool:
        if state is None:
            state = self.state
        if sum(state) != len(state):
            print(
                f"Something is wrong. Maybe the rules are not well encoded. {self} (real state: {state})"
            )
        return max(state) == len(state)

    def solve(self):
        print(self._solve(self.state, []))

    def _solve(self, state: List, history: List):
        if self.debug:
            print(f"debug: {state}, {history}")

        if self.check(state):
            self.set_state(state).set_history(history)
            return self
        if len(history) >= self.max_iter:
            return None
        if str(state) in self._seen:
            return None

        self._seen.add(str(state))
        for move in ["square", "circle", "triangle"]:
            try:
                result = self._solve(self.rules[move](state), [*history, move])
            except KeyError:
                pass
            if result:
                return result


class Level_0(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {"square": lambda state: [0, 2]}
        super().__init__(
            level=0, max_iter=1, cardinality=2, rules=rules, *args, **kwargs
        )


class Level_1(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda state: [0, 2],
            "circle": lambda state: [1, 1],
        }
        super().__init__(
            level=1, max_iter=1, cardinality=2, rules=rules, *args, **kwargs
        )


class Level_2(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda state: [state[2], *state[:2]],
            "circle": lambda state: [state[1], 0, state[0] + state[2]],
        }
        super().__init__(
            level=2, max_iter=2, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_3(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda state: [state[2], 0, state[0] + state[1]],
            "circle": lambda state: [state[2], *state[:2]],
        }
        super().__init__(
            level=3, max_iter=3, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_4(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [s[1], s[0], s[2]],
            "circle": lambda s: [0, s[0] + s[1], s[2]],
            "triangle": lambda s: [s[0], s[2], s[1]],
        }
        super().__init__(
            level=4, max_iter=4, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_5(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [s[1], s[0] + s[2], 0],
            "circle": lambda s: [s[2], s[0], s[1]],
        }
        super().__init__(
            level=5, max_iter=4, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_6(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [0, s[0] + s[1], s[2]],
            "circle": lambda s: [s[2], s[0], s[1]],
        }
        super().__init__(
            level=6, max_iter=4, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_7(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [0, s[0] + s[2], s[1]],
            "circle": lambda s: [s[0], s[2], s[1]],
            "triangle": lambda s: [s[2], s[1], s[0]],
        }
        super().__init__(
            level=7, max_iter=4, cardinality=3, rules=rules, *args, **kwargs
        )


class Level_8(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [0, s[1], s[3], s[0] + s[2]],
            "circle": lambda s: [s[0]+s[1], s[3], s[2], 0],
            "triangle": lambda s: [s[3], s[1], s[0], s[2]],
        }
        super().__init__(
            level=8, max_iter=3, cardinality=4, rules=rules, *args, **kwargs
        )


class Level_9(SyncroGame):
    def __init__(self, *args, **kwargs):
        rules = {
            "square": lambda s: [s[2], s[0], s[1], s[3]],
            "circle": lambda s: [s[0], s[1], s[2] + s[3], 0],
            "triangle": lambda s: [0, s[0] + s[1], s[2], s[3]],
        }
        super().__init__(
            level=9, max_iter=5, cardinality=4, rules=rules, *args, **kwargs
        )
