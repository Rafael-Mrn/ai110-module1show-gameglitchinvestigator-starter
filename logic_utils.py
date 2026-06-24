import random


def new_game(low: int = 1, high: int = 100):
    #FIX: Refactored new_game into logic_utils.py using agent mode
    """
    Build the fresh session state for a brand-new game.

    Returns a dict of state values to apply to st.session_state. This is the
    single source of truth for what a "new game" means, so no reset can be
    forgotten by a caller:
      - secret:   a new target within the difficulty range
      - attempts: reset to 0
      - status:   reset to "playing"   (fixes: was left as "won"/"lost",
                  so the status guard kept calling st.stop())
      - history:  cleared              (fixes: stale guesses carried over)
    """
    return {
        "secret": random.randint(low, high),
        "attempts": 0,
        "status": "playing",
        "history": [],
    }


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    raise NotImplementedError("Refactor this function from app.py into logic_utils.py")


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Straight numeric comparison; guess and secret are always ints.
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📈 Go HIGHER!"
    return "Too Low", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number.

    A win on the first attempt scores 100, decreasing by 10 per attempt and
    floored at 10. Every wrong guess ("Too High"/"Too Low") costs 5 points.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome in ("Too High", "Too Low"):
        return current_score - 5

    return current_score
