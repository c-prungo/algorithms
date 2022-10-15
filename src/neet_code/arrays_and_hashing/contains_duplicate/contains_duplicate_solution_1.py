from typing import List


def contains_duplicate(nums: List[int]):

    nums.sort()
    for _ in range(len(nums) - 1):

        n = nums.pop(0)
        if n == nums[0]:
            return True

    return False
