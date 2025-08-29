# This code is going to do something similar to solver_quick but it will search through a dictionary to be more accurate

from itertools import permutations, combinations
from wordfreq import zipf_frequency

with open("/usr/share/dict/words") as f:
    ENGLISH_WORDS = set(w.strip().lower() for w in f)

def is_word(word: str) -> bool:
    """
    Returns true if the word is in the english dictionary (local dictionary to MacOS)
    """
    return word.lower() in ENGLISH_WORDS

def generate_words(letters: str, min_len: int = 3, max_len: int | None = None) -> list:
    """
    Generates all unique permutations of the given letters for lengths 3,...,N
    Returns the words (optionally ranked by frequency)
    """
    s = letters.lower()
    n = len(s)
    
    if max_len is None:
        max_len = n
    
    max_len = min(max_len, n)
    min_len = max(min_len, 1)
    
    words = []
    for length in range(min_len, max_len + 1):
        for idxs in combinations(range(n), length): #produces all possible combinations of indices of said length (idxs)
            comb = ''.join(s[i] for i in idxs)
            for perm in permutations(comb):
                word = ''.join(perm)
                if is_word(word):
                    words.append(word)
    return sorted(words, key=lambda word: (len(word), zipf_frequency(word, 'en'), word), reverse=True)

if __name__ == '__main__':
    print(generate_words('stare'))


### Okay, so this code is working but it gives answers that might also be wrong or acronyms for things that are not necessarily considered words
# I think the best way to do this would be to use a dictionary of words and then check each word against that dictionary
# This would be much more accurate and would also allow for acronyms (e.g., STARE)
