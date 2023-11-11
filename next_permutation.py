class Solution(object):
    def nextPermutation(self, a):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        i = 0
        for i in range(n-2, -2, -1):
            if i == -1 or a[i] < a[i+1]:
                break;
        if i == -1:
            return a.sort()
        j = None
        for j in range(i+2, n+1):
            if j == n or a[j] <= a[i]:
                break
        j = j-1
        a[i], a[j] = a[j], a[i]
        a[i+1:] = sorted(a[i+1:])
        return a
