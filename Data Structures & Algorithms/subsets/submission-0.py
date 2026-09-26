class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            result.append(path[:])
            
            for elem in range(start, len(nums)):
                path.append(nums[elem])

                backtrack(elem + 1, path)

                path.pop()

        backtrack(0, [])

        return result



