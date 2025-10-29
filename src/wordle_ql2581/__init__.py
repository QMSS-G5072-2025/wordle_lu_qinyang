# read version from installed package
from importlib.metadata import version, PackageNotFoundError
from .main import (
    validate_guess,
    check_guess,
    is_valid_word,
    calculate_game_score,
)

try:
    __version__ = version("wordle_ql2581")
except PackageNotFoundError:
    # Package is not installed, read from pyproject.toml or use a default
    __version__ = "0.1.3"

__all__ = [
    "validate_guess",
    "check_guess",
    "is_valid_word",
    "calculate_game_score",
]