import os

from src.bimatrix_game import find_nash_equilibria, find_admissible_equilibria
from src.utils import read_matrices_from_txt


def play_bimatrix_game(config):
    file_path = config.csv_path
    current_dir = os.path.dirname(__file__)

    csv_path = os.path.join(current_dir, file_path)

    A, B = read_matrices_from_txt(csv_path)
    nash_equilibria = find_nash_equilibria(A, B)
    admissible_equilibria = find_admissible_equilibria(A, B)
    print("Nash Equilibria:", nash_equilibria)
    print("Admissible Equilibria:", admissible_equilibria)

