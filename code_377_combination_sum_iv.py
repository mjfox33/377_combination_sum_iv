class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0]*target

        for current_sum in range(target+1):
            for num in nums:
                if num > target:
                    break
                if current_sum == num:
                    dp[current_sum] += 1
                if current_sum > num:
                    dp[current_sum] += dp[current_sum-num]
        return dp[-1]