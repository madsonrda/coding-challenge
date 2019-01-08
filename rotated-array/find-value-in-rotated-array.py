class Solution(object):
    def find_pivot(self,array,start,end):

        while start <= end:
            mid = (end+start)/2
            if array[mid+1] < array[mid]:
                return mid+1
            if array[start] <= array[mid]:
                start=mid+1
            else:
                end = mid-1
        return -1
    def binary_search(self,array,target,start,end):

        while start <= end:
            mid = (end+start)/2
            if array[mid] == target:
                return mid
            if target < array[mid]:
                end = mid-1
            else:
                start = mid + 1
        return -1
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        if len(nums) == 2:
            for i,n in enumerate(nums):
                if n == target:
                    return i
            return -1

        start = 0
        end = len(nums)-1
        if nums[start] <= nums[end]:
            return self.binary_search(nums,target,start,end)
        pivot = self.find_pivot(nums,start,end)

        if target == nums[pivot]:
            return pivot

        if target <= nums[end]:
            return self.binary_search(nums,target,pivot+1,end)
        else:
            return self.binary_search(nums,target,start,pivot -1)
def main():
    array = map(int,raw_input().split())
    target = int(raw_input())
    Solution.search(array,target)
