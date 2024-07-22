import logging
import hydra
import dotenv

from omegaconf import DictConfig

dotenv.load_dotenv()

log = logging.getLogger(__name__)


@hydra.main(config_path="configs", version_base="1.3")
def main(config: DictConfig):
    if config.name == 'play_bimatrix_game':
        from src import play_bimatrix_game
        return play_bimatrix_game(config)


if __name__ == '__main__':
    main()
