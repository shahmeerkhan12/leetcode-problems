def max_rectangle(hist: list[int]):
    res = 0
    n = len(hist)
    # calculate rectangles of all heights in the hist
    for i in range(n):
        cur = hist[i]
    # left bars atleast height is equal to cur bar till u reach the first element
        j = i-1
        while j>=0 and hist[j] >= hist[i]:
            cur += hist[i]
            j -= 1
        j = i+1
        while j<n and hist[j] >= hist[i]:
            cur += hist[i]
            j += 1

        res = max(res, cur)

    return res

histogram = [1,3,4,3,1]
print(max_rectangle(histogram))
