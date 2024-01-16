def findPairs(arr):
    n = len(arr)
    Hash = {}

    for i in range(n-1):
        for j in range(i+1,n):
            sum = arr[i]+arr[j]
            if sum in Hash.keys():

                prev = Hash.get(sum) # Hash[sum]
                print(str(prev) + " and (%d %d)" % (arr[i], arr[j]))
                return True
            else:
                Hash[sum] = (arr[i], arr[j])
    return False

arr = [8, 1, 2, 7, 3, 9, 5]
print(findPairs(arr))
