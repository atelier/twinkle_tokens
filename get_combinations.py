import re
import itertools
import math


def get_syllable_combinations(line_syllables=7, min_word_syllables=1, max_word_syllables=4):
    def get_possibilities_for_word_length(word_syllables):
        max_occurrences = 0
        if word_syllables > line_syllables:
            max_occurrences = 0
        elif word_syllables == line_syllables:
            max_occurrences = 1
        else:
            max_occurrences = math.floor(
                line_syllables/word_syllables
            )
        return [n for n in range(0, max_occurrences+1)]

    possibilities_for_words = []

    for word_syllables in range(min_word_syllables, max_word_syllables+1):
        possibilities_for_words.append(
            get_possibilities_for_word_length(word_syllables)
        )

    valid_combinations = []
    occurrences = []

    combinations = [n for n in itertools.product(*possibilities_for_words)]

    for combination in combinations:
        total_syllables = 0
        for i, occurrences_in_line in enumerate(combination):
            word_syllables = i + min_word_syllables
            total_syllables += word_syllables * occurrences_in_line
            # print("word syllables "+str(word_syllables)+"     occurrences"+str(occurrences_in_line))
        # print("total syllables "+str(total_syllables))
        if total_syllables == line_syllables:
            valid_combinations.append(combination)
    return valid_combinations

def get_orderings(combinations):
    """
    combinations = {
        2: 2,
        3: 1
    }
    """
    line = []
    for syllables, occurrences in combinations.items():
        for i in range(occurrences):
            line.append(syllables)
    varied_lines = []
    for n in itertools.permutations(line):
        if n not in varied_lines:
            varied_lines.append(n)
    return varied_lines

def get_line_variations(line_syllables=7, min_word_syllables=1, max_word_syllables=4):
    orderings = []

    combinations = get_syllable_combinations(
        line_syllables=line_syllables,
        min_word_syllables=min_word_syllables,
        max_word_syllables=max_word_syllables
    )

    for i, combination in enumerate(combinations):
        combinations_dictionary = {}
        for i, occurrences in enumerate(combination):
            if occurrences == 0:
                continue
            combinations_dictionary[i+min_word_syllables] = occurrences
        orderings += get_orderings(combinations_dictionary)

    return orderings

def get_accentuated_line(line, words):
    accentuated_words = []
    line = re.sub('-', '', line)
    counter = 0
    for word_syllables in words:
        accentuated_words.append(line[counter:counter+word_syllables])
        counter += word_syllables
    return accentuated_words

def get_accentuated_variations(line, min_word_syllables=2, max_word_syllables=5):
    variations = get_line_variations(
        line_syllables=len(re.sub('-', '', line)),
        min_word_syllables=min_word_syllables,
        max_word_syllables=max_word_syllables
    )
    return [get_accentuated_line(line, v) for v in variations]

if __name__ == "__main__":
    print(get_accentuated_variations("10-10-10-1"))
