
def selectionSort(arr):
    n = len(arr)
    temp = None
    for i in range(n):
        for j in range(n-i-1):
            if arr[i] > arr[i+j+1]:
                temp = arr[i]
                arr[i] = arr[i+j+1]
                arr[i+j+1] = temp

    return arr

def sort2(arr):
    n = len(arr)
    temp = None
    for i in range(n):
        min = 99999999
        ind = None
        for j in range(n-i):
            if arr[i+j] > min:
                ind = i+j
        if ind:
            temp = arr[i]
            arr[i] = arr[ind]
            arr[ind] = temp

    return arr
        



ar1 = [34, 29, -23, 832, 32, 24, 432, -293, 34]
print(selectionSort(ar1))
print(sort2(ar1))