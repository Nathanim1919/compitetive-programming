def uniquePath(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """

    db = [[0] * n for _ in range(m)]

    for i in range(1, m):
        db[i][0] = 1

    for j in range(1, n):
        db[0][j] = 1

    for i in range(1, m):
        for j in range(1, n):
            db[i][j] = db[i - 1][j] + db[i][j - 1]

    return db[m - 1][n - 1]



print(uniquePath(3, 7)) # 28
print(uniquePath(3, 2)) # 3
print(uniquePath(2, 3)) # 3