class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        column = len(matrix[0])-1
        
        for row_index in range(0,int((column+1)/2)) :
            # print(row_index)
            for index in range(row_index,column-row_index):
                # print(index)
                if index<column:
                    row = row_index
                    col = index
                    temp = matrix[row_index][index]
                    while True:
                        temp,  matrix[col][column-row] = matrix[col][column-row], temp
                        # matrix[col][column-row] = element
                        row ,col = col, column-row
                        # print("row:{}, column:{}".format(row,col))
                        if row==row_index and col==index:
                            # print(row)
                            break;
        # print(matrix)
                
