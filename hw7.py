from wordle_ql2581 import validate_guess, check_guess, calculate_game_score

# Example usage
print("Validate 'apple':", validate_guess("apple"))
print("Check guess 'react' against 'crane':", check_guess("crane", "react"))
print("Game score for 3 guesses:", calculate_game_score(3))

# Check documentation examples
help(validate_guess)
help(check_guess)
