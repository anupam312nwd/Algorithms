def maximumSum(arr):
    n = len(arr)
    answer = arr[0]
    suf_del = 0
    suf_no_del = arr[0]

    for i in range(1, len(arr)):
        suf_del = max(suf_del + arr[i], suf_no_del)
        suf_no_del = max(suf_no_del + arr[i], arr[i])
        answer = max(answer, suf_del, suf_no_del)
        print(suf_no_del, suf_del, answer)
    return answer


arr = [8, -1, 2, 3, -2, -3, 7]
# print(maximumSum(arr))
maximumSum(arr)
