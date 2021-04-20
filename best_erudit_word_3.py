#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from classes import *
from collections import Counter
from functools import reduce


MULTIPLICATOR = [
                    Multiplicator(27, [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]),
                    Multiplicator(18, [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1])

                ][0]

VOCABULARY = 'vocab/' + [
                "15_letter_words_sushestvitelnie.txt",
                "all_15_letter_words.txt",
                "dummy.txt"
              ][0]


def main():
    words = read_15_letter_words()
    filtered_words = filer_out_out_not_possible_words(words)
    enrich_with_values(words)
    sort_by_value(filtered_words)
    analysis = analyse_vocab(words)

    print(analysis)
    for w in filtered_words[:5]:
        print(w)


def analyse_vocab(words):
    analysis = VocabAnalysis()
    for w in words:
        analysis.letter_count.update(Counter(w.word))
    return analysis


def read_15_letter_words():
    with open(VOCABULARY, encoding='utf-8', mode="r") as f:
        words = [Word(w) for w in f.read().split("\n")]
    return words


def filer_out_out_not_possible_words(words):
    return list(filter(lambda x: bag_has_sufficient_letters_for_word(x), words))


def sort_by_value(filtered_words):
    filtered_words.sort(key=lambda w: w.value, reverse=True)


def enrich_with_values(words):
    for w in words:
        w.value = get_word_value(w)
    return words


def get_word_value(word):
    word_length = len(MULTIPLICATOR.letters)

    letter_values = [letters_value_map[c] for c in word.word]

    multi = MULTIPLICATOR.letters
    letter_values_multiplied = [0] * word_length
    for i in range(len(letter_values)):
        letter_values_multiplied[i] = letter_values[i] * multi[i]

    word_full_value = sum(letter_values_multiplied) * MULTIPLICATOR.word

    return word_full_value


def bag_has_sufficient_letters_for_word(word):
    counter = Counter(word.word)
    for c in counter:
        if counter[c] > letters_in_the_bag[c]:
            return False
    return True


if __name__ == '__main__':
    main()
