
def find_nash_equilibria(A, B):
    """
        Finds all Nash equilibria for a given bimatrix game.

        Parameters:
        A (np.ndarray): Payoff matrix for Player 1, where A[i, j] represents the payoff for Player 1 when Player 1 chooses strategy i and Player 2 chooses strategy j.
        B (np.ndarray): Payoff matrix for Player 2, where B[i, j] represents the payoff for Player 2 when Player 1 chooses strategy i and Player 2 chooses strategy j.

        Returns:
        List[Tuple[int, int]]: A list of tuples representing the indices of Nash equilibria. Each tuple (i, j) indicates that the pair of strategies (i, j) is a Nash equilibrium.

        Example:
        A = np.array([[1, 0],
                      [2, -1]])

        B = np.array([[2, 3],
                      [1, 0]])

        find_nash_equilibria(A, B)
        Output: [(0, 0), (1, 1)]

        Description:
        A pair of strategies (i, j) is a Nash equilibrium if the following conditions are satisfied for all rows and columns:
            1. For Player 1: A[i, j] <= A[k, j] for all k
            2. For Player 2: B[i, j] <= B[i, k] for all k
        These conditions ensure that neither player can improve their payoff by unilaterally changing their strategy.
        """
    nash_equilibria = []
    rows, cols = A.shape

    for i in range(rows):
        for j in range(cols):
            # Check condition (3.1a) for Player 1
            condition_1 = all(A[i, j] <= A[k, j] for k in range(rows))

            # Check condition (3.1b) for Player 2
            condition_2 = all(B[i, j] <= B[i, k] for k in range(cols))

            if condition_1 and condition_2:
                nash_equilibria.append((i, j))

    return nash_equilibria


def find_admissible_equilibria(A, B):
    """
        Finds all admissible Nash equilibria for a given bimatrix game.

        Parameters:
        A (np.ndarray): Payoff matrix for Player 1, where A[i, j] represents the payoff for Player 1 when Player 1 chooses strategy i and Player 2 chooses strategy j.
        B (np.ndarray): Payoff matrix for Player 2, where B[i, j] represents the payoff for Player 2 when Player 1 chooses strategy i and Player 2 chooses strategy j.

        Returns:
        List[Tuple[int, int]]: A list of tuples representing the indices of admissible Nash equilibria. Each tuple (i, j) indicates that the pair of strategies (i, j) is an admissible Nash equilibrium.

        Example:
        A = np.array([[1, 0],
                      [2, -1]])

        B = np.array([[2, 3],
                      [1, 0]])

        find_admissible_equilibria(A, B)
        Output: [(1, 1)]

        Description:
        This function first identifies all Nash equilibria using the `find_nash_equilibria` function. It then determines which of these equilibria are admissible.
        A Nash equilibrium (i1, j1) is considered admissible if there does not exist another Nash equilibrium (i2, j2) such that:
            1. A[i1, j1] <= A[i2, j2] and B[i1, j1] <= B[i2, j2], and
            2. At least one of these inequalities is strict.
        In other words, an admissible Nash equilibrium is one that is not strictly worse than any other Nash equilibrium for both players.
        """
    nash_equilibria = find_nash_equilibria(A, B)
    admissible_equilibria = nash_equilibria.copy()

    for (i1, j1) in nash_equilibria:
        for (i2, j2) in nash_equilibria:
            if (i1, j1) != (i2, j2):
                if (A[i1, j1] <= A[i2, j2] and B[i1, j1] <= B[i2, j2]) and (
                        A[i1, j1] < A[i2, j2] or B[i1, j1] < B[i2, j2]):
                    if (i2, j2) in admissible_equilibria:
                        admissible_equilibria.remove((i2, j2))

    return admissible_equilibria
