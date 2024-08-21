class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_arr = []

        while nums1 and nums2:
            if nums1[0] <= nums2[0]:
                merged_arr.append(nums1[0])
                nums1.pop(0)
            else:
                merged_arr.append(nums2[0])
                nums2.pop(0)
        
        merged_arr += nums1 + nums2

        if len(merged_arr) % 2:
            median = merged_arr[len(merged_arr) // 2]
        else:
            median = (merged_arr[len(merged_arr) // 2 - 1] + merged_arr[len(merged_arr) // 2]) / 2

        return median
    
solution = Solution()
print(solution.findMedianSortedArrays([1,2],[3,4]))
