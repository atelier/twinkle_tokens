import pandas as pd
import random
import nltk
from get_combinations import get_accentuated_variations


pronunciations = nltk.corpus.cmudict.dict()

def get_pronun(word):
    word = word.lower()
    matches = pronunciations.get(word)
    if matches:
        # if len(matches) > 1:
        #     print("WARNING: more than one pronunciation for '%s' found: %s" % (word, matches))
        return matches[0]
    return ["?0"]

def get_stress(word):
    # Get singable components (vowel like)
    # Return only stress
    parts = tuple([char[-1] for char in get_pronun(word) if char[-1].isdigit()])
    parts = ''.join(parts)
    return parts

def phrase_stress_pattern(phrase, as_string=True):
    pattern = [get_stress(token) for token in nltk.word_tokenize(phrase)]
    if as_string:
        return '-'.join([''.join(p) for p in pattern])
    return pattern

def create_corpus():
    words = []
    sources = [
        'austen-emma.txt',
        'austen-persuasion.txt',
        'austen-sense.txt',
        'bible-kjv.txt',
        'blake-poems.txt',
        'bryant-stories.txt',
        'burgess-busterbrown.txt',
        'carroll-alice.txt',
        'chesterton-ball.txt',
        'chesterton-brown.txt',
        'chesterton-thursday.txt',
        'edgeworth-parents.txt',
        'melville-moby_dick.txt',
        'milton-paradise.txt',
        'shakespeare-caesar.txt',
        'shakespeare-hamlet.txt',
        'shakespeare-macbeth.txt'
    ]
    for source in sources:
        corpus = nltk.corpus.gutenberg.raw(source)
        corpus_words = ' '.join(corpus.split('\n')).split(' ')
        words += corpus_words
    return words

def create_dataframe():
    words = create_corpus()
    df = pd.DataFrame(
        [
            {'stress': get_stress(word), 'word': word} for word in words
        ] + [
            {
                'stress': '10101',
                'word': 'unparentheses'
            },
            {
                'stress': '0101',
                'word': 'and more and more'
            },
            {
                'stress': '1001',
                'word': 'melody fat'
            },
            {
                'stress': '10111',
                'word': 'ready no new far'
            },
            {
                'stress': '111',
                'word': 'bad bad bad'
            },
            {
                'stress': '10010',
                'word': 'never a faster'
            },
            {
                'stress': '0111',
                'word': 'but no no no'
            },
            {
                'stress': '00',
                'word': 'sh sh'
            }
        ]
    )
    return df

def generate_line_matching_syllables(line):
    variations = get_accentuated_variations(
        line, min_word_syllables=2, max_word_syllables=5
    )
    # [['101', '0101'], ['1010', '101'], ['10', '10101'], ['10101', '01'], ['10', '10', '101'], ['10', '101', '01'], ['101', '01', '01']]
    variation = random.choice(variations)
    df = create_dataframe()
    words = []
    for target in variation:
        target = "^" + target + "$"
        matches = df.stress.str.match(target)
        options = df[matches].word
        try:
            words.append(options.sample(1).values[0])
        except:
            print(target)
            words.append('No')
    return words
    # ['1010', '101']

if __name__ == "__main__":
    song = [
        "Twinkle twinkle little star",
        "How I wonder what you are",
        "Up above the world so high",
        "Like a diamond in the sky",
        "Twinkle twinkle little star",
        "How I wonder what you are",
        "When the blazing sun is gone",
        "When he nothing shines upon",
        "Then you show your little light",
        "Twinkle twinkle all the night",
        "Twinkle twinkle little star",
        "How I wonder what you are",
    ]
    parsed_song = []
    for line in song:
        parsed_song.append(phrase_stress_pattern(line))
    # print(parsed_song)
    new_song = []
    for line in parsed_song:
        new_song.append(generate_line_matching_syllables(line))
    print(new_song)
