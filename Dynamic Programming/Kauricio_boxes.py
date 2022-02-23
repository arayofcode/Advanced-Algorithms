"""
Kauricio has n cardboard boxes. i-th box has dimensions (x_i, y_i, z_i).

Kauricio also has a machine that can expand or shrink box by adding or 
subtracting 1 from all dimensions. The machine can be repeatedly used on
any box as long as dimensions remain valid. 

Kauricio wants to shrink/ expand so that sum of boxes is exactly V
"""
import math

# DP Approach
boxes = [(1, 2, 3), (4, 2, 6), (1, 1, 1)]
V = 55

def approach(V = V, i = len(boxes), boxes =  boxes):
    if V >= 0 and i > 0:
        minUse = 99999999999999999999999999999999
        cRoot = int(math.ceil((V) ** (1/3) + 1))
        for k in range(0, 1):
            l, b, h = boxes[i-1]
            # print(boxes[i-1])
            s = k + approach(V - math.prod((l + k, b + k, h + k)), i-1, boxes)
            print(s)
            if s < minUse:
                minUse = s
        print(minUse)
        return minUse

approach()
