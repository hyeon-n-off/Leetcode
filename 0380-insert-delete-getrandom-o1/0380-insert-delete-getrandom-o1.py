import random

class RandomizedSet:

    def __init__(self):
        self.set = set()

    def insert(self, val: int) -> bool:
        before = len(self.set)
        self.set.add(val)
        after = len(self.set)

        return False if before == after else True

    def remove(self, val: int) -> bool:
        before = len(self.set)
        self.set.discard(val)
        after = len(self.set)

        return False if before == after else True

    def getRandom(self) -> int:
        return random.choice(list(self.set))