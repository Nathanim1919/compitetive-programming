from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    """
    Calculates the minimum number of coins needed to make up a given amount.

    Args:
        coins (List[int]): List of coin denominations available.
        amount (int): Target amount to make up.

    Returns:
        int: Minimum number of coins needed to make up the target amount. Returns -1 if it is not possible to make up the amount.

    """
    db = [float('inf')] * (amount + 1)
    db = [0]

    for i in range(1, (amount + 1)):
        for coin in coins:
            if (i - coin) >= 0:
                db[i] = min(db[i], db[i - coin] + 1)
    return db[amount] if db[amount] != float('inf') else -1
