class Solution(object):
    def rotate(self, a):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(a)
        m = len(a[0])
        #make a transpose matrix
        for i in range(n):
            for j in range(i+1, m):
                a[i][j], a[j][i] = a[j][i], a[i][j]
        
        #swap columns of transpose matrix
        for i in range(n):
            for j in range(m/2):
                a[i][j], a[i][m-j-1] = a[i][m-j-1], a[i][j]
