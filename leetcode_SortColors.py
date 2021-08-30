class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #[정렬됨|정렬안됨|정렬됨]
        #       red   blue
        #red는 0이 들어갈 위치 (정렬이 안된 맨 왼쪽 부분)
        #white는 이동할 데이터의 위치, 
        #blue는 2가 들어갈 위치의 다음 위치를 가르킴 (정렬이 완료 된 오른쪽 파트의 맨 왼쪽 부분)
    
        red, white, blue = 0, 0, len(nums)
        while white < blue:
            if nums[white] < 1:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
                
        return nums