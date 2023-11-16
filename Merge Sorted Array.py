class Solution(object):
    def merge(self, a, n, b, m):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        i = n-1
        j = m-1
        k = n+m-1
        while i >= 0 and j >= 0:
            if a[i] > b[j]:
                a[k] = a[i]
                k -= 1
                i -= 1
            else:
                a[k] = b[j]
                k -= 1
                j -= 1
        while i >= 0:
            a[k] = a[i]
            k -= 1
            i -= 1
        while j >= 0:
            a[k] = b[j]
            k -= 1
            j -= 1
        
