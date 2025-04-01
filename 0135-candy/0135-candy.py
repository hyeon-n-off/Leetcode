class Solution:
    def candy(self, ratings: list[int]) -> int:
        desending, flag = [], False
        total = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i - 1] < ratings[i]:
                total[i] = total[i - 1] + 1

                if flag:
                    desending.append([start, end])
                    flag = False

            elif ratings[i - 1] > ratings[i]:
                if flag:
                    end = i
                else:
                    start, end = i - 1, i
                    flag = True

            else:
                total[i] = 1

                if flag:
                    desending.append([start, end])
                    flag = False
        
        if flag:
            desending.append([start, end])
            flag = False

        for start, end in desending:
            for i in range(end - start):
                if total[end - i - 1] < total[end - i] + 1:
                    total[end - i - 1] = total[end - i] + 1
        
        return sum(total)