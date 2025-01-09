\\\
[1,8,6,2,5,4,8,3,7]
area = height * length

length => the range of the two numbers
height => min of the two sticks

(brute force)
cur_max = 
lower_pointer = 0
higher_pointer = 8
-> we want the new min to be higher
-> the min out of the lower and higher
-> if the min is lower move up
if the min is down move down
length = range of the lower and the higher painter
height = min (lower_pointer and the higher_pointer)

[1,8,6,2,5,4]                 
while index higher_pointer > index lower pointer     
(last index - index current node)
with the lower pointer being 1 -> range(len -1) *                       (min of the lower point and that point)

(Optimal)
-> move the pointer to the one that has a more max value



\\\

class Solution:
    def maxArea(self, height: List[int]) -> int:
        cur_max = 0
        lower_pointer = 0
        higher_pointer = len(height) - 1
        while higher_pointer > lower_pointer:
            length = higher_pointer - lower_pointer
            width = min(height[higher_pointer], height[lower_pointer])
            cur_max = max(cur_max, length * width)
            if height[higher_pointer] > height[lower_pointer]:
                lower_pointer += 1
            else:
                higher_pointer -=1
        return cur_max