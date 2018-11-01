class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_list = []
        d = {}
        for i, num in enumerate(nums):
            if target - num in d:
                index_list.append([d[target - num], i])
            d[num] = i
        return index_list
        # no special case handling becasue it's assumed that it has only one solution
            
