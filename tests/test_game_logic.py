from logic_utils import check_guess, new_game, update_score

# check_guess returns (outcome, message); these tests pin the outcome string.

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- update_score tests ---
# Scoring contract:
#   Win on attempt 1 = +100, decreasing by 10 per attempt, floored at 10.
#   Every wrong guess ("Too High"/"Too Low") = -5, regardless of attempt parity.

def test_first_attempt_win_scores_100():
    assert update_score(0, "Win", 1) == 100

def test_later_win_scores_less():
    # Attempt 3 win: 100 - 10*(3-1) = 80, added to existing score.
    assert update_score(20, "Win", 3) == 100

def test_win_points_floored_at_10():
    # Deep into a game the win payout never drops below 10.
    assert update_score(0, "Win", 50) == 10

def test_too_high_always_penalizes():
    # Regression: a wrong "Too High" guess must subtract, never add, on any attempt.
    assert update_score(50, "Too High", 2) == 45
    assert update_score(50, "Too High", 3) == 45

def test_too_low_penalizes_equally():
    # Both wrong outcomes are treated symmetrically.
    assert update_score(50, "Too Low", 2) == 45
    assert update_score(50, "Too Low", 3) == 45

def test_unknown_outcome_leaves_score_unchanged():
    assert update_score(42, "Unknown", 1) == 42


# --- Regression tests for the "New Game" bug ---
# Before the fix, the New Game handler reset attempts/secret but left
# status as "won"/"lost" and never cleared history. That stale status
# tripped the `status != "playing"` guard (st.stop()), so the user could
# not submit a new guess. These tests pin down new_game()'s reset contract.

def test_new_game_resets_status_to_playing():
    # The core regression: status MUST come back to "playing", otherwise
    # the status guard in app.py stops the script before Submit can run.
    state = new_game(1, 100)
    assert state["status"] == "playing"

def test_new_game_clears_history():
    # History must be a fresh empty list, not carried over from the last game.
    state = new_game(1, 100)
    assert state["history"] == []

def test_new_game_resets_attempts_to_zero():
    state = new_game(1, 100)
    assert state["attempts"] == 0

def test_new_game_secret_within_difficulty_range():
    # Secret should respect the passed range, not a hardcoded 1-100.
    low, high = 1, 50
    for _ in range(100):
        secret = new_game(low, high)["secret"]
        assert low <= secret <= high
