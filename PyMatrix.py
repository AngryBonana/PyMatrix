def input_matrix(str_num, column_num, type_m):
    matrix = []
    for i in range(str_num):
        matrix.append(str(input()).split())
        if len(matrix[i]) < column_num:
            matrix[i] = matrix[i] + [0] * (column_num - len(matrix[i]))
        elif len(matrix[i]) > column_num:
            p = matrix[i]
            while len(p) > column_num:
                p.pop()
            else:
                matrix[i] = p
        if type_m == "int" or type_m == "i":
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
        elif type_m == "float" or type_m == "fl" or type_m == "f":
            for j in range(len(matrix[i])):
                matrix[i][j] = float(matrix[i][j])
    return matrix
        
        
def print_matrix(matrix):
    max_len = 0
    for i in range(len(matrix)):
        for j in matrix[i]:
            if len(str(j)) > max_len:
                max_len = len(str(j))
    for i in range(len(matrix)):
        if i == 0:
            print("/ ", end="")
        elif i == len(matrix) - 1:
            print("\\ ", end="")
        else:
            print("| ", end="")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]: ^{max_len}} ", end="")
        if i == 0:
            print(" \\")
        elif i == len(matrix) - 1:
            print(" /")
        else:
            print(" |")
    
            