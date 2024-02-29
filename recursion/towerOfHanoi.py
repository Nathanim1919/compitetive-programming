def Hanoi(n, src, dst, tmp):
    print(n)
    if n > 0:
        Hanoi((n - 1), src, tmp, dst)
        print("Moving disk", n, "from", src, "to", dst)
        Hanoi((n - 1), tmp, dst, src)
    else:
        return


Hanoi(3, "A", "C", "B")




# recursive code explanation


# step 1:
    #
