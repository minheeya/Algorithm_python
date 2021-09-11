#merge sort

def MergeSort(arr):

    def split(start, end):  #분할
        if start>=end:
            return
        
        middle = (start + end) // 2
        split(start, middle)
        split(middle+1, end)
        merge(start, middle, end)

    def merge(start, middle, end):  #병합
        temp = []
        first, second = start, middle+1

        while first<=middle and second<=end:
            if arr[first] <= arr[second]:
                temp.append(arr[first])
                first+=1
            else:
                temp.append(arr[second])
                second+=1
        
        while first<=middle:
            temp.append(arr[first])
            first+=1

        while second<=end:
            temp.append(arr[second])
            second+=1

        for i in range(start, end+1):
            arr[i] = temp[i-start]
        
    return split(0,len(arr)-1)


data = [80, 75, 10, 60, 15, 49, 12, 25]
MergeSort(data)
print(data)
