# This Code:
# Generates all unique permutations of your letters for lengths 2..N
# Checks each candidate against the English lexicon (via wordfreq.zipf_frequency(word, 'en'))
### i.e., this is not the most accurate version since this is looking at the frequency of words, not whether or not the word is in the dictionary 
### furthermore since it simply compares to a wide variety of corpora, it may contain words that are not in the dictionary (e.g., slang)
### however, the benefit is that it is much faster than the other version, which was checking each word against the dictionary (external)
# Returns the words (optionally ranked by frequency)

from itertools import permutations, combinations
from wordfreq import zipf_frequency

def is_word(word: str, lang: str = 'en', min_zipf = 1.5) -> bool:
    """
    Returns true if the word is frequently used in the given language (English by default)
    Note that the threshold is set at 1.5, which is arbitrary and may need to be adjusted further (the higer, the stricter and more frequent the word)
    """
    return zipf_frequency(word, lang) >= min_zipf

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