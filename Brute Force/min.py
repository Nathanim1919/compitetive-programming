from typing import List


def getMin(nums: List[int]) -> int:
    min = nums[0]

    for i in range(len(nums)):
        if nums[i] < min:
            min = nums[i]

    return min



if __name__ == "__main__":
    print(getMin([2,3,5,-9,5,2]))