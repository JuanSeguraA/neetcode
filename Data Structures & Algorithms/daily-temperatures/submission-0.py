class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        waiting_days = []  

        for today in range(n):
            while waiting_days and temperatures[today] > temperatures[waiting_days[-1]]:
                earlier_day = waiting_days.pop()
                result[earlier_day] = today - earlier_day

            waiting_days.append(today)

        return result