import random

class Matrix:
    rows = 3
    coluns = 3
    matrix = []

    def construct_matrix():
        for x in range(Matrix.rows):
            line = []
            for y in range(Matrix.coluns):
                line.append(random.randint(0, 9)*10)
            Matrix.matrix.append(line)
        for a in Matrix.matrix:
            print(a)
        
    def mod_map(mult):
        matrix_r = []

        for l in Matrix.matrix:
            result_line = []

            for element in l:
                result = element + w
                result_line.append(result)
            
            matrix_r.append(result_line)
        return matrix_r
        
def print_mr():
    for a in Matrix.matrix_r:
        print(a)



print("Original Matrix: \n")
#Matrix Original
Matrix.construct_matrix()

print(" \n")

#Multiplicador
w = 2

#Matrix final
result_matrix = Matrix.mod_map(w)
print("Final Matrix:")
for l in result_matrix:
    print(l)
