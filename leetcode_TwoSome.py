#초기 내가 생각했던 방법
#class Solution(object):
#    def twoSum(self, nums, target):
#        nums_dic = {}  #nums_dic = [값 : 인덱스, ...]
#        for idx, num in enumerate(nums):
#            nums_dic[num] = idx
#            if target - num in nums_dic and idx != nums_dic[target - num]:
#                return [idx, nums_dic[target - num]]
# = > nums = [3, 3] / target = 6인 case 통과 X


class Solution(object):
    def twoSum(self, nums, target):
        nums_dic = {}  #nums_dic = [값 : 인덱스, ...]
        for idx, num in enumerate(nums):
            if target - num in nums_dic and idx != nums_dic[target - num]:
                return [idx, nums_dic[target - num]]
            nums_dic[num] = idx
#비교후에  nums_dic[num] = idx을 추가해줌으로써, 같은 값을 더해 target이 되는 경우에 
#겹치지 않는 인덱스를 return 할 수 있다.