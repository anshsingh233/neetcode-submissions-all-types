class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea=0
        st=[]
        for i , h in enumerate(heights):
            start=i
            while st and st[-1][1]>h:
                index,height=st.pop()
                maxarea=max(maxarea,height*(i-index))
                start=index
            st.append((start,h))
        for i,h in st:
            maxarea=max(maxarea,h*(len(heights)-i))
        return maxarea