def mergeSort(array1, array2):
    i, j = 0, 0
    mergedArray = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergedArray.append(arr1[i])
            i += 1
        else:
            mergedArray.append(arr2[j])
            j += 1
    
    return mergedArray + arr1[i:] + arr2[j:]
        