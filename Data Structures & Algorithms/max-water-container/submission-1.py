class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L,R=0,len(heights) -1
        capacity=0

        while L<R:
            water = min(heights[L],heights[R]) * (R-L)
            capacity= max(capacity,water)

            if heights[L]<heights[R]:
                L+=1
            else:
                R -=1

        return capacity