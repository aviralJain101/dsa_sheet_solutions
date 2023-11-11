class Solution(object):
    def sortColors(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        l = 0
        r = n-1
        i = 0
        while i <= r:
            if a[i] == 0:
                a[i], a[l] = a[l], a[i]
                i += 1
                l += 1
            elif a[i] == 2:
                a[i], a[r] = a[r], a[i]
                r -= 1
            else:
                i += 1
