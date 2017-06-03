# coding: utf-8

import string

import nltk
import pandas as pd

# nltk.download()



twinkle1 = "Twinkle twinkle little star"
twinkle2 = "How I wonder what you are"
sentence = "In 1913 I had the happy idea to fasten a bicycle wheel to a kitchen stool and watch it turn."

print("Loading pronunciation dictionary")
pronunciations = nltk.corpus.cmudict.dict()

def get_pronun(word, silent=True):
    word = word.lower()
    matches = pronunciations.get(word)
    if matches:
        if len(matches) > 1:
            if not silent:
                print("WARNING: more than one pronunciation for '%s' found: %s" % (
                    word, matches))
        return matches[0]
    if not silent:
        print("WARNING: no pronunciation match for '%s' found" % word)
    return ["?0"]

def get_vowels(word):
  # Get singable components (vowel like)
  # Strip stress
  parts = tuple([char[:-1] for char in get_pronun(word) if char[-1].isdigit()])
  return parts

def get_stress(word):
  # Get singable components (vowel like)
  # Return only stress
  parts = tuple([char[-1] for char in get_pronun(word) if char[-1].isdigit()])
  return parts

def phrase_stress_pattern(phrase, as_string=True):
    pattern = [get_stress(token) for token in nltk.word_tokenize(phrase)]
    if as_string:
        return '-'.join([''.join(p) for p in pattern])
    return pattern

def phrase_syllable_pattern(phrase, as_string=True):
    pattern = [len(get_vowels(token)) for token in nltk.word_tokenize(phrase)]
    if as_string:
        return ''.join([str(p) for p in pattern])
    return pattern

def phrase_vowel_pattern(phrase, as_string=True):
    pattern = [get_vowels(token) for token in nltk.word_tokenize(phrase)]
    if as_string:
        return '-'.join(['_'.join(p) for p in pattern])
    return pattern

# from nltk.tokenize.moses import MosesDetokenizer
# def detokenize(tokens):
#     detokenizer = MosesDetokenizer()
#     return detokenizer.detokenize(tokens, return_str=True)


#print( get_vowels('twinkle') )
#print( get_pronun('twinkle') )
#print( get_stress('twinkle') )
phrase = twinkle1

print()
print( "Original Phrase: '%s'" % phrase)
print( "Vowel Pattern:", phrase_vowel_pattern(phrase, as_string=False) )
print( "Stress Pattern:", phrase_stress_pattern(phrase, as_string=False) )
print( "Syllable Pattern:", phrase_syllable_pattern(phrase, as_string=False) )
print()
print( "Vowl Pattern String:", phrase_vowel_pattern(phrase, as_string=True) )
print( "Stress Pattern String:", phrase_stress_pattern(phrase, as_string=True) )
print( "Syllable Pattern String:", phrase_syllable_pattern(phrase, as_string=True) )
print()


print("Loading corpus")
corpus = nltk.corpus.gutenberg.raw('whitman-leaves.txt')
flatten = lambda l: [item for sublist in l for item in sublist]

# Split lines:
phrases = corpus.split('\n')
# Split on commas:
phrases = flatten([p.split(',') for p in phrases])
# Strip out punctuation
phrases = [p for p in phrases if p and p not in string.punctuation]


print("Parsing corpus")
phrase_dict = [{
     'phrase': phrase,
     'syllables': phrase_syllable_pattern(phrase),
     'stress': phrase_stress_pattern(phrase),
     'vowels': phrase_vowel_pattern(phrase)} for phrase in phrases
]

df = pd.DataFrame(phrase_dict)

target = phrase_stress_pattern(twinkle1)
matches = df[df.stress == target]
partial_matches = df[df.stress.str.contains(target)]

print("Matching phrases:", matches)

import ipdb; ipdb.set_trace()
