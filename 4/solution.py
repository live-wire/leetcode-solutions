class Solution:
    def merge_array_inplace(self,nums1,nums2):
        
        nums1_size = len(nums1)
        nums2_size = len(nums2) 
        nums1_index = nums1_size-1
        nums2_index = nums2_size-1
        
        while (nums1_index >= 0 ) and (nums2_index >=0 ):
            if nums1[nums1_index] > nums2[nums2_index]:
                nums1[nums1_index], nums2[nums2_index] = nums2[nums2_index], nums1[nums1_index]
                nums2_index = nums2_index-1
            else:
                nums2_index = nums2_index - 1
        median_index =  int((nums1_size+nums2_size)/2)
        print(nums1)
        print(nums2)
        # print(median_index)
        if (nums1_size+nums2_size)%2==0:
            if median_index==nums1_size:
                return (nums1[median_index-1]+nums2[median_index-nums1_size])/2
            elif median_index>nums1_size:
                return (nums2[median_index-1]+nums2[median_index])/2
            else:
                return (nums1[median_index-1]+nums1[median_index])/2
        else:
            if median_index>nums1_size-1:
                return nums2[median_index-nums1_size]
            else:
                return nums1[median_index]
        

    
    def merge_arrays(self,nums1,nums2) -> float:
        nums1_index = 0
        nums2_index = 0
        nums1_size = len(nums1)
        nums2_size = len(nums2)
        merged_array = []
        while (nums1_index < nums1_size) and (nums2_index < nums2_size):
            if nums1[nums1_index] < nums2[nums2_index]:
                merged_array.append(nums1[nums1_index])
                nums1_index = nums1_index+1
            else:
                merged_array.append(nums2[nums2_index])
                nums2_index= nums2_index+1
        
        if nums1_index<nums1_size:
            while nums1_index<nums1_size:
                merged_array.append(nums1[nums1_index])
                nums1_index = nums1_index+1
        else:
            while nums2_index<nums2_size:
                merged_array.append(nums2[nums2_index])
                nums2_index = nums2_index+1
        print(merged_array)
        if len(merged_array)%2==0:
            index = int(len(merged_array)/2)
            return (merged_array[index]+merged_array[index-1])/2.0
        else:
            return float(merged_array[int(len(merged_array)/2)])
        
        
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return float(self.merge_arrays(nums1,nums2))
