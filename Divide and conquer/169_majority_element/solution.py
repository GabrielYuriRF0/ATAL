class Solution(object):
    def majorityElement(self, nums):
        size = len(nums) // 2
        hashMap = {}

        if len(nums) == 1:
            return nums[0]
        else:
            for num in nums:
                if num not in hashMap.keys():
                    hashMap[num] = 1
                else:
                    if hashMap[num] == size:
                        return num
                    hashMap[num] += 1
        
        