class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #bindok
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        preMap = {}
        for i , val in enumerate(nums):
            diff = target - val
            if diff in preMap:
                return [preMap[diff], i]
            preMap[val] = i
        return
