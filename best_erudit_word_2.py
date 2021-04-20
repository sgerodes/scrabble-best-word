#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from classes import *

import codecs
from collections import Counter


multiplicator = [
                    Multiplicator(27, [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]),
                    Multiplicator(18, [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1])

                ][0]


def main():
    words = read_15_letter_words()
    filtered_words = filter(lambda x: bag_has_sufficient_letters_for_word(x), words)
    words_with_value = {w: {"value": word_value(w)} for w in filtered_words}
    most_valuable = find_most_valuable_word(words_with_value)
    print (most_valuable['word'])
    print (most_valuable['value'])


def dummy_words():
    return [u"абдоминализация", u"абиссопелагиаль", u"абсолютирование", u"жжжолютирование"]


def find_most_valuable_word(words):
    most_valuable_word = ''
    most_valuable_value = 0
    for w in words:
        if words[w]["value"] > most_valuable_value:
            most_valuable_word = w
            most_valuable_value = words[w]["value"]
    return {"word": most_valuable_word, "value": most_valuable_value}


def read_15_letter_words():
    with open("vocab/15_letter_words_sushestvitelnie.txt", encoding='utf-8', mode="r") as f:
        words = f.read().split("\n")
    return words


def word_value(word):
    word_length = len(multiplicator.letters)

    letter_values = [letters_value_map[c] for c in word]

    multi = multiplicator.letters
    letter_values_multiplied = [0] * word_length
    for i in range(len(letter_values)):
        letter_values_multiplied[i] = letter_values[i] * multi[i]

    word_full_value = sum(letter_values_multiplied) * multiplicator.word

    return word_full_value


def bag_has_sufficient_letters_for_word(word):
    counter = Counter(word)
    for c in counter:
        if counter[c] > letters_in_the_bag[c]:
            return False
    return True


main()
