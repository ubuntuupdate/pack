
def jobScheduling(arr, t):

    n = len(arr)
    
    for i in range(n):
        for j in range(n-i-1):
            if arr[i][2] < arr[i+j][2]:
                temp = arr[i]
                arr[i] = arr[i+j]
                arr[i+j] = temp

    print(arr)

    slots = [False] * t
    
    job = ['-1'] * t

    for i in range(n):
        for j in range(min(t-1, arr[i][1]-1), -1, -1):
            if not slots[j]:
                slots[j] = True
                job[j] = arr[i][0]
                break

    print(job)


arr = [['a', 2, 100],
        ['b', 1, 19],
        ['c', 2, 27],
        ['d', 1, 25],
        ['e', 3, 15]]

jobScheduling(arr, 3)