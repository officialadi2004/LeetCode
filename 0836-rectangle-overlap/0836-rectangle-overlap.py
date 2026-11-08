class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        # Two rectangles overlap if and only if their 1D projections
        # on both the X-axis and Y-axis have an intersection of positive length.
        return (rec1[0] < rec2[2] and 
                rec2[0] < rec1[2] and 
                rec1[1] < rec2[3] and 
                rec2[1] < rec1[3])