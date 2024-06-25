def swapString(s1: str, s2: str) -> bool:
    chars = {}
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            chars[i] = s1[i]
            count += 1
        if count == 2:
            break


    # chars = reversed(chars)
    #swap chars
    for key, value in chars.items():
        s2[key] = value
        print(s1, s2)




if __name__ == "__main__":
    swapString("bank", "kanb")

