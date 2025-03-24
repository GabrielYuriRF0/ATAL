class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binarySearch(nums, left, right):
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            elif left >= right:
                return -1
            elif target > nums[middle]:
                result = binarySearch(nums, middle+1, right)
            elif target < nums[middle]:
                result = binarySearch(nums, left, middle)
            return result

        return binarySearch(nums, 0, len(nums) - 1)
            


solution = Solution()
print(solution.search([-1,0,3,5,9,12],2))