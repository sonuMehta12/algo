class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        def merge_list(arr1 , arr2):
            i = j = 0
            while ( i< len(arr1) and j < len(arr2) ):
                if(arr1[i] < arr2[j]):
                    arr.append(arr1[i])
                    i=i+1
                else:
                    arr.append(arr2[j])
                    j = j+1
            while(i < len(arr1)):
                arr.append(arr1[i])
                i = i + 1
            while(j < len(arr2)):
                arr.append(arr2[j])
                j=j+1


        #find the median of two sorted array
        def find_midian(arr1, arr2):
            merge_list(arr1, arr2)
            mid = len(arr) // 2
            isEven = True if len(arr) // 2  == mid else False
            median=0
            if isEven:
                median = (arr[mid - 1] + arr[mid ]) /2
            else:
                median = arr[mid -1]
            return median   

        a = [1,2]
        b = [3,4]
        c = find_midian(a, b)
        return c
           
