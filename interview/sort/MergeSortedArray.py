class MergeSortedArray():
    def mergeSortedArray(self):
        nums1=[1,2,3]
        nums2=[2,5,6]
        m=len(nums1)
        n=len(nums2)
        idx1=0
        idx2=0
        merge_list=[]
        while(idx1<m and idx2<n):
            if nums1[idx1] <= nums2[idx2]:
                merge_list.append(nums1[idx1])
                idx1+=1
            else:
                merge_list.append(nums2[idx2])
                idx2+=1

        while idx1<m:
            merge_list.append(nums1[idx1])
            idx1+=1

        while idx2<n:
            merge_list.append(nums2[idx2])
            idx2+=1

        print("merge_list:", merge_list)

    def mergeSortedArrayWithoutThirdArray(self):
        '''
            You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
            and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
            Merge nums1 and nums2 into a single array sorted in non-decreasing order.
            The final sorted array should not be returned by the function, but instead be
            stored inside the array nums1. To accommodate this, nums1 has a length of m + n,
            where the first m elements denote the elements that should be merged, and the last n elements are
            set to 0 and should be ignored. nums2 has a length of n.
        '''
        nums1=[1,2,3,0,0,0]
        nums2=[2,5,6]
        m=3
        n=3
        idx1=m-1
        idx2=n-1
        k=m+n-1
        while(idx1>=0 and idx2>=0):
            if nums1[idx1]>nums2[idx2]:
                nums1[k]=nums1[idx1]
                idx1=idx1-1
            else:
                nums1[k]=nums2[idx2]
                idx2=idx2-1
            k=k-1

        while(idx2>=0):
            nums1[k]=nums2[idx2]
            k=k-1
            idx2=idx2-1

        print(nums1)

if __name__=="__main__":
    mergeSortedArray = MergeSortedArray()
    mergeSortedArray.mergeSortedArray()