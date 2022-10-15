from typing import List, Tuple


def two_sum(nums: List[int], target: int) -> List[int]:

    new_nums = [n for n in nums if n <= target else None]