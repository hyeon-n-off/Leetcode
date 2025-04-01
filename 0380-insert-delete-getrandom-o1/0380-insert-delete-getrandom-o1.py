import random

class RandomizedSet:
    def __init__(self):
        self.num_to_index = {}  # 값 -> 인덱스 저장
        self.values = []  # 실제 값들을 저장하는 리스트

    def insert(self, val: int) -> bool:
        if val in self.num_to_index:
            return False
        self.num_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.num_to_index:
            return False
        
        # 마지막 요소와 삭제할 요소의 위치 교환
        last_val = self.values[-1]
        idx = self.num_to_index[val]
        
        self.values[idx] = last_val
        self.num_to_index[last_val] = idx

        # 마지막 요소 삭제
        self.values.pop()
        del self.num_to_index[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)
