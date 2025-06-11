def problem1():

    '''
    matrix = [
        [1 (11), 2 (12), 3 (13)],
        [4 (21), 5 (22), 6 (23)],
        [7 (31), 8, 9]
    ]
    len(matrix) =  columns --> i
    len(matrix[0]) = rows  --> j
    transpose(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    [
        [1, 4],
        [2, 5],
        [3, 6]
    ]
    transpose(matrix)
    '''

    def transpose(matrix):
        '''
        returns the transpose matrix 

        '''
        transpose_matrix = []
        
        for i in range(len(matrix[0])): #column
            row = []
            for j in range(len(matrix)): #row
                row.append(matrix[j][i])
            transpose_matrix.append(row)

        return transpose_matrix

    # test cases 
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(transpose(matrix))

    matrix0 = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(transpose(matrix0))

'''
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)
'''
def reverse_list(lst):
    r = len(lst) - 1 # Right Pointer 
    l = 0            # Left Pointer

    # Index through the list with the left and right pointers 
    while (l < r):
        # print("Boo")
        lst[l], lst[r] = lst[r] , lst[l]

        l += 1
        r -= 1
    return lst
        

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
print(reverse_list(lst))

