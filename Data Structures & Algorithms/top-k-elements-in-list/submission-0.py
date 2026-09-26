class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            key = num
            if key not in frequency:
                frequency[key] = 1
            else:
                frequency[key] += 1

        sorted_nums = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

        i = k
        top_k = []
        for top in sorted_nums:
            if i > 0:
                top_k.append(top[0])
                i -= 1
        return top_k


        # frq_lst = []
        # i = len(frequency) - k
        # while i > 0:
        #     for x in frequency.values():
        #         frq_lst.append(x)
        #         frq_lst.pop(frq_lst.index(min(frq_lst)))
        #     i -= 1

        # return frq_lst
