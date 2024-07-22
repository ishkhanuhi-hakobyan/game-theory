import numpy as np


def read_matrices_from_txt(file_path):
    A = []
    B = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        current_matrix = None
        for line in lines:
            line = line.strip()
            if line == 'Matrix A:':
                current_matrix = A
            elif line == 'Matrix B:':
                current_matrix = B
            elif line:
                current_matrix.append([int(num) for num in line.split(', ')])
    A = np.array(A)
    B = np.array(B)

    return A, B
