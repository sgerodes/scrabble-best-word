#!/usr/bin/env python
# -*- coding: utf-8 -*-
from constants import *
from classes import *
from collections import Counter
import logging
import logging.config

MULTIPLICATOR = [
                    Multiplicator(9, [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]),
                    Multiplicator(8, [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 3, 1, 1, 1]),
                    Multiplicator(6, [1, 1, 1, 1, 1, 1, 3, 1, 3, 1, 1, 1, 1, 1, 1]),
                ][0]
WORDS_LENGTH = 15
VOCABULARY = [
                WordFile("vocab/15_letter_words_sushestvitelnie.txt", "utf-8"),
                WordFile("vocab/all_15_letter_words.txt", "utf-8"),
                WordFile("../../IdeaProjects/russian-words/russian_utf8.txt", "utf-8"),
                WordFile("vocab/word_rus_blog.harrix.org_article_3334.txt", "utf-8"),
                WordFile("../Russian-Nouns/dist/russian_nouns.txt", "utf-8"),
                WordFile("../Russian-Nouns/dist/russian_nouns_without_filter.txt", "utf-8"),
                WordFile("vocab/wordhelper_ru/wordhelper_ru_15_letter_words_2_list.txt", "utf-8"),
                WordFile("vocab/rus-yaz_niv_ru/words_filtered.txt", "utf-8"),
                WordFile("vocab/erudit_1-1_su/words.txt", "utf-8"),
              ][5]


logger = logging.getLogger(__name__)
logging.config.fileConfig("logging.conf")

def main():
    print(get_word_value(Word("четырехугольник")))
    words = read_words()
    for w in words:
        if w.word in "четырехугольник":
            print(w.word)
    filtered_words = filer_out_out_not_possible_words(words)
    enrich_with_values(filtered_words)
    sort_by_value(filtered_words)
    analysis = analyse_vocab(filtered_words)

    print(analysis)
    for w in filtered_words[:5]:
        print(w)


def analyse_vocab(words):
    analysis = VocabAnalysis()
    for w in words:
        analysis.letter_count.update(Counter(w.word))
    return analysis


def read_words():
    print(f"Reading {VOCABULARY.path}")
    with open(VOCABULARY.path, encoding=VOCABULARY.encoding, mode="r") as f:
        words = [Word(w) for w in f.read().split("\n")]
    return words


def filer_out_out_not_possible_words(words):
    words = filter(lambda x: len(x.word) == WORDS_LENGTH, words)
    words = filter(lambda x: bag_has_sufficient_letters_for_word(x), words)
    return list(words)


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
        if c not in letters_in_the_bag or counter[c] > letters_in_the_bag[c]:
            return False
    return True


if __name__ == '__main__':
    main()
