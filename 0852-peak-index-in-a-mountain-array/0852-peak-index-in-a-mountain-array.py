class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        i = 1
        j = len(arr) - 2
        while i <= j:
            mid = (i+j)//2
            if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            elif arr[mid] < arr[mid-1] and arr[mid] > arr[mid+1]:
                j = mid - 1
            else:
                i = mid + 1