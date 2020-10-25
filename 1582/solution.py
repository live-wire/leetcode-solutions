import numpy as np
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        result = 0
        mat = np.array(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (mat[i,j] == 1):
                    if (sum(mat[i,:]) == 1) and (sum(mat[:,j]) == 1):
                        result += 1
                        
        return result