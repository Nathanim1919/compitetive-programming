from typing import List

# fractional knapsack: find the maximum value that can be put in a knapsack of capacity W
def fractional_knapsack(items: List[tuple], capacity: int) -> float:
    total_value = 0
    # fill the capacity
    for item in sorted(items, key=lambda x: x[1] / x[0], reverse=True):
        print(item)
        if (item[0] <= capacity):
            total_value += item[1]
            capacity -= item[0]
        else:
            total_value += item[1] * capacity/item[0]
            capacity = 0
            break
    return total_value


# Example usage
if __name__ == "__main__":
    items = [(10, 60), (20, 100), (30, 120)]
    capacity = 50
    print(f"Maximum value in knapsack: {fractional_knapsack(items, capacity)}") # 240