def grade(action, correct, step_count):
    score = 0.0

    action = action.lower()

    # classification score
    if correct in action:
        score += 0.6
    elif "important" in action and correct == "spam":
        score -= 0.5  # dangerous mistake

    # efficiency reward
    if step_count <= 2:
        score += 0.2

    # penalty for overthinking
    if step_count > 4:
        score -= 0.2

    return max(0.0, min(1.0, score))