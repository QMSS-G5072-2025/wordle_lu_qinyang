def validate_guess(guess, word_length=5):
    """
    Validates if a guess is valid for Wordle.

    Parameters
    ----------
    guess : str
        The word guess to validate.
    word_length : int, optional
        Expected length of the word (default 5).

    Returns
    -------
    bool
        True if guess is valid, False otherwise.

    Examples
    --------
    >>> validate_guess("apple")
    True
    >>> validate_guess("Apple")
    False
    >>> validate_guess("appl3")
    False
    >>> validate_guess("app")
    False
    """
    if not isinstance(guess, str):
        return False
    if len(guess) != word_length:
        return False
    if not guess.isalpha():
        return False
    return guess.islower()


def check_guess(secret_word, guess):
    """
    Checks a guess against the secret word and returns color hints.

    Parameters
    ----------
    secret_word : str
        The secret word to guess.
    guess : str
        The player's guess.

    Returns
    -------
    list of tuple
        Each tuple contains (letter, color) where color is one of:
        'green' (correct letter and position),
        'yellow' (correct letter, wrong position),
        or 'gray' (letter not in word).

    Examples
    --------
    >>> check_guess("apple", "apron")
    [('a', 'green'), ('p', 'green'), ('r', 'gray'), ('o', 'gray'), ('n', 'gray')]
    >>> check_guess("crane", "reach")
    [('r', 'yellow'), ('e', 'yellow'), ('a', 'green'), ('c', 'yellow'), ('h', 'gray')]
    """
    if len(secret_word) != len(guess):
        return []

    result = []
    secret_list = list(secret_word)
    guess_list = list(guess)

    # First pass: mark exact matches (green)
    for i in range(len(guess_list)):
        if guess_list[i] == secret_list[i]:
            result.append((guess_list[i], 'green'))
            secret_list[i] = None
            guess_list[i] = None
        else:
            result.append((guess_list[i], None))

    # Second pass: mark partial matches (yellow or gray)
    for i in range(len(guess_list)):
        if guess_list[i] is not None:
            if guess_list[i] in secret_list:
                result[i] = (guess_list[i], 'yellow')
                secret_list[secret_list.index(guess_list[i])] = None
            else:
                result[i] = (guess_list[i], 'gray')

    return result


def is_valid_word(word, word_list):
    """
    Checks if a word exists in the valid word list.

    Parameters
    ----------
    word : str
        The word to check.
    word_list : list
        List of valid words.

    Returns
    -------
    bool
        True if word is in the list, False otherwise.
    """
    return word.lower() in [w.lower() for w in word_list]


def calculate_game_score(guesses_used, max_guesses=6):
    """
    Calculates the score for a completed Wordle game.

    Parameters
    ----------
    guesses_used : int
        Number of guesses used to solve the puzzle.
    max_guesses : int, optional
        Maximum allowed guesses (default 6).

    Returns
    -------
    int
        Score from 0 to max_guesses (higher is better).
    """
    if guesses_used <= 0 or guesses_used > max_guesses:
        return 0
    return max_guesses - guesses_used + 1



# Test / demo code
if __name__ == "__main__":
    print("Testing validate_guess:")
    print(validate_guess("apple"))  # True
    print(validate_guess("Apple"))  # False
    print(validate_guess("appl3"))  # False
    print(validate_guess("app"))  # False

    print("\nTesting check_guess:")
    print(check_guess("apple", "apron"))  # [('a', 'green'), ('p', 'green'), ...]
    print(check_guess("crane", "reach"))  # [('r', 'yellow'), ('e', 'yellow'), ...]

    print("\nTesting is_valid_word:")
    word_list = ["apple", "crane", "reach"]
    print(is_valid_word("apple", word_list))  # True
    print(is_valid_word("banana", word_list))  # False

    print("\nTesting calculate_game_score:")
    print(calculate_game_score(3))  # 4 (6-3+1)
    print(calculate_game_score(6))  # 1
    print(calculate_game_score(0))  # 0 (invalid)
