from code_377_combination_sum_iv import Solution

def test_example_1():
    s = Solution()
    nums = [1,2,3]
    target = 4
    output = 7
    assert s.combinationSum4(nums,target) == output

def test_example_2():
    s = Solution()
    nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    target = 10
    output = 9
    assert s.combinationSum4(nums,target) == output