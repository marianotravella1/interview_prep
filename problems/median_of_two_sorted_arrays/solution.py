class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = []
        index1 = 0
        index2 = 0
        len1 = len(nums1)
        len2 = len(nums2)

        while index1 < len1 and index2 < len2:
            if nums1[index1] <= nums2[index2]:
                merged_array += [nums1[index1]]
                index1 += 1
            else:
                merged_array += [nums2[index2]]
                index2 += 1
                

        if index1 < len1:
            merged_array += nums1[index1:]
                
        else:
            merged_array += nums2[index2:]
            
        
        n = len(merged_array)
        mid_index = n // 2  
        if n % 2 == 1:
            return float(merged_array[mid_index])
        
        
        else:
            val1 = merged_array[mid_index - 1]
            val2 = merged_array[mid_index]
            return (val1 + val2) / 2.0






        