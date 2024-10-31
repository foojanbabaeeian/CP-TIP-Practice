def sum(arr):
    if not arr:
        return 0
    return arr[0] + sum(arr[1:])

arr = [ 1, 2, 3, 4 ]
print(sum(arr))