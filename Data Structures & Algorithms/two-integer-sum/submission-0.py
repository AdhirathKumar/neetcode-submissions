class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save_required_difference = {}
        for i in range(len(nums)):
            if nums[i] not in save_required_difference:
                save_required_difference[target - nums[i]] = i
            else:
                return [save_required_difference[nums[i]], i]