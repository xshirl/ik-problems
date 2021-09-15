def merger_first_into_second(arr1, arr2):
    #
    # Write your code here.
    #
    k = len(arr2) - 1
    i = len(arr1) - 1
    j = (len(arr2)//2) -1
    while i >= 0 and j >= 0:
        if arr1[i] <= arr2[j]:
            arr2[k] = arr2[j]
            j -= 1
        else:
            arr2[k] = arr1[i]
            i -=1
        k -= 1
    while i >= 0 and k >= 0:
        arr2[k] = arr1[i]
        i -= 1
        k -=1
    return arr2