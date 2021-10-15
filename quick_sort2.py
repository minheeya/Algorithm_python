#quick sort

def QuickSort(arr):

    if len(arr)<=1: 
        return arr   #리스트 반환

    pivot = arr[len(arr)-1]  #pivot값은 끝값으로 지정
    lesser,  equal, greater = [], [], []  #3개의 리스트 생성
    for num in arr:
        if num < pivot:  
            lesser.append(num)   #pivot값보다 작은 값은 lesser에 추가
        elif num > pivot:
            greater.append(num)  #pivot값보다 큰 값은 greater에 추가
        else:
            equal.append(num)    #pivot값과 같은 값은 equal에 추가

    return QuickSort(lesser) + equal + QuickSort(greater)  #리스트 합 반환

data = [80, 75, 10, 60, 15, 49, 12, 25]
print(data)      #퀵 정렬 하기 전 data 출력
after_data = QuickSort(data)
print(after_data) #data를 정렬한 리스트 after_data 출력
