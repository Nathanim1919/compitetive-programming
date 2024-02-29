def NDaysOfChristmas(gifts, n):
    for i in range(n, 1, -1):
        print(f"On the {i}th day of Christmas, my true love gave to me")
        for j in range(i, 2, -1):
            print(f"{j} {gifts[j]}, ", end="")
        if i > 1:
            print("and ")
    print("a partridge in a pear tree.")


gifts = [
    "",
    "two turtle doves",
    "three french hens",
    "four calling birds",
    "five golden rings",
    "six geese a laying",
    "seven swans a swimming",
    "eight maids a milking",
    "nine ladies dancing",
    "ten lords a leaping",
    "eleven pipers piping",
    "twelve drummers drumming",
]
n = len(gifts) - 1
NDaysOfChristmas(gifts, n)