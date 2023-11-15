class Solution(object):
    def merge(self, a):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a.sort()
        stack = []
        for i in a:
            if len(stack) == 0:
                stack.append(i)
                continue
            t = stack.pop()
            if t[1] >= i[0]:
                stack.append([min(i[0], t[0]), max(i[1], t[1])])
            else:
                stack.append(t)
                stack.append(i)
        return stack
