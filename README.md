# Game Theory

## Requirements:

- [anaconda](https://docs.anaconda.com/free/anaconda/install/index.html): Version == 24.5.0

## Installation

- Clone the repository with the following command `git clone git@github.com:ishkhanuhi-hakobyan/game-theory.git`

After **_cloning_** the repository:

- Open the terminal and navigate to the root directory of the project.
- Run the command `conda env update -f environment.yaml` to install all the required dependencies.
- Run the command `conda activate game-theory` to activate the created environment.



## Scripts documentation

The entry point for all scripts is the `run.py` file located in the root directory.

- `play_bimatrix_game.py`:
  This script is responsible for playing bimatrix game between two players. To play the game with the desired matrices, edit the .txt file which is located under the path 'src/bimatrix_game/matrix_txt/matrices.txt'.
  - **Command to run the script:** `python run.py --config-name=play_bimatrix_game`


  