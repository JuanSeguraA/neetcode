class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solution = []
        nums_sorted = sorted(nums)
        n = len(nums_sorted)

        for i in range(n):
            if i > 0 and nums_sorted[i] == nums_sorted[i - 1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                total = nums_sorted[i] + nums_sorted[left] + nums_sorted[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    solution.append([nums_sorted[i], nums_sorted[left], nums_sorted[right]])
                    left += 1
                    right -= 1
                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1
                    while left < right and nums_sorted[right] == nums_sorted[right + 1]:
                        right -= 1

        return solution