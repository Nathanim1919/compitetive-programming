def checkAllNumsInMaxtric(matrixs: list[list[int]]) -> bool:
    nums = [i for i in range(1, len(matrixs[0])+1)]
    print(nums)

    for i in matrixs: # [[1,2,3], [1, 2, 3]]
        for j in nums:
            if j not in i:
                return False
    return True
    

if __name__ == "__main__":
    # generate more test cases
    # test case 1 nxn matrix
    matrix = [[1,2,3], [1,2,3], [1,2,3]]
    print(checkAllNumsInMaxtric(matrix)) # True

    # test case 2 nxn matrix
    matrix = [[1,2,3], [1,2,3], [1,2,4]]
    print(checkAllNumsInMaxtric(matrix)) # False
    
