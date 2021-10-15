#quick sort
   
def QuickSort(arr):

    def sort(start, end): #정렬 할 인덱스 범위 지정하여 정렬이 실행되는 함수로 보냄
        if start>=end:    #길이가 1이하 일 경우 함수 종료
            return 

        pivot = partition(start,end)
        sort(start,pivot-1)   #pivot값 보다 작은 값들의 집합 정렬
        sort(pivot+1,end)    #pivot값 보다 큰 값들의 집합 정렬

    def partition(left, right): #정렬 & 분할지점(pivot위치) 반환
        pivot = right
        while left < right: 
            while arr[left] < arr[pivot] and left < right: 
                left+=1
            while arr[right] >= arr[pivot] and left < right:
                right-=1
            if left<right:
                arr[left], arr[right] = arr[right], arr[left] #left right값 교환
        arr[left], arr[pivot] = arr[pivot], arr[left]   #left와 right가 엇갈리면 left와 pivot값 교환
        return left  #새로운 pivot의 위치 left반환

    return sort(0,len(arr)-1)

data = [80, 75, 10, 60, 15, 49, 12, 25]
QuickSort(data)
print(data)      #퀵 정렬 후 data 출력