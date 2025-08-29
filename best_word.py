from itertools import combinations
from more_accurate import generate_words

def all_groups(letters: str, k: int = 5) -> list[str]:
    """All k-letter combinations (order doesn't matter)."""
    return [''.join(group) for group in combinations(letters, k)]

def best_group(letters: str) -> tuple[str, int]:
    """
    Returns (group, score) where score = number of words generateable from that group.
    """
    best_g, best_score = "", -1
    for g in all_groups(letters, 5):
        words = generate_words(g)          # assume this returns a list of words
        score = len(words)
        if score > best_score:
            best_g, best_score = g, score
    return best_g, best_score


if __name__ == '__main__':
    print(best_group('abcdefghijklmnopqrstuvwxyz'))
