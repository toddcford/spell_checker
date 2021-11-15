import re 
from collections import Counter

def words(text): 
  return re.findall(r'\w+', text.lower())

WORDS       = Counter(words(open('Data/big.txt').read()))
TOTAL_WORDS = sum(WORDS.values())

def wordProbability(word):
  return WORDS[word] / TOTAL_WORDS

def best_guess(word):
  return max(potential_words(word), key=wordProbability)

def potential_words(word):
  return (known([word]) or known(one_edit(word)) or  known(two_edits(word)) or [word])

def known(words):
  return set(w for w in words if w in WORDS)

def one_edit(word):
  letters    = 'abcdefghijklmnopqrstuvwxyz'
  splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
  deletes    = [ L + R[1:] for L, R in splits if R]
  transposes = [ L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
  replaces   = [ L + c + R[1:] for L, R in splits if R for c in letters ]
  inserts    = [ L + c + R for L, R in splits for c in letters]
  return set(deletes + transposes + replaces + inserts)

def two_edits(word):
  return set(e2 for e1 in one_edit(word) for e2 in one_edit(e1))


def correct_sentence(input):
  words = input.split(' ')
  new_words = [best_guess(w.lower()) for w in words]
  for i in range(len(new_words)):
    if new_words[i] == 'i':
      new_words[i] = 'I'

  return ' '.join(new_words)






