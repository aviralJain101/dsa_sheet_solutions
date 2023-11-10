class Solution(object):
    def setZeroes(self, a):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        is_col0 = False
        n = len(a)
        m = len(a[0])
        for i in range(n):
            for j in range(m):
                if a[i][j] == 0:
                    if j == 0:
                        is_col0 = True
                    else:
                        a[i][0] = 0
                        a[0][j] = 0
        for i in range(1, n):
            for j in range(1, m):
                if a[i][0] == 0 or a[0][j] == 0:
                    a[i][j] = 0
        if a[0][0] == 0:
            for j in range(m):
                a[0][j] = 0

        if is_col0:
            for i in range(n):
                a[i][0] = 0
        
        
