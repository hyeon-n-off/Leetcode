class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        citations.sort()
        h_index = 0

        for i, _ in enumerate(range(n), start=1):
            if i <= citations[n - i]:
                h_index += 1
            else:
                break

        return h_index