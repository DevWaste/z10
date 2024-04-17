import random

def generate_matrix(rows, cols):
    return [[random.randint(-200, 200) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0]) if rows else 0
    return [[matrix_a[i][j] + matrix_b[i][j] for j in range(cols)] for i in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

# Генерация матриц
matrix_1 = generate_matrix(10, 10)
matrix_2 = generate_matrix(10, 10)

# Сложение матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

# Вывод матриц
print("Matrix 1:")
print_matrix(matrix_1)
print("\nMatrix 2:")
print_matrix(matrix_2)
print("\nMatrix 3 (Sum of Matrix 1 and Matrix 2):")
print_matrix(matrix_3)
