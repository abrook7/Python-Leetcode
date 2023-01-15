class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_diff = {'max_diff':0, 'min':0}
        running_total = 0

        for num in range(len(nums)):
            running_total += nums[num]

            if running_total - max_diff['min'] > max_diff['max_diff'] or num == 0:
                max_diff['max_diff'] = running_total - max_diff['min']
            if running_total < max_diff['min']:
                max_diff['min'] = running_total

        return max_diff['max_diff']