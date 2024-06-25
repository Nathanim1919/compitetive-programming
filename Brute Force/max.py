def getMax(nums) -> int:
    max = nums[0]

    for i in range(len(nums)):
        if nums[i] > max:
            max  = nums[i]
    return max



if __name__ == "__main__":
    print(getMax([1,2,3,7,8,9,2,34,66,8]))