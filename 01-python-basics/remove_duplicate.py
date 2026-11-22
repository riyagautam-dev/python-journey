class Solution:
    def removeDuplicates(self, nums):
        j = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]

        return j + 1


nums = [1, 1, 2, 2, 3, 3, 4]

obj = Solution()
length = obj.removeDuplicates(nums)

print("New length:", length)
print("Unique elements:", nums[:length])