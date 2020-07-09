#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from collections import Counter

multiplicators = {"word_multiplicator": 27,
                  "letter_multiplicator": [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1]}

letters_value_map = {u'а': 1,
                     u'б': 3,
                     u'в': 2,
                     u'г': 2,
                     u'д': 3,
                     u'е': 2,
                     u'ё': 2,
                     u'ж': 5,
                     u'з': 5,
                     u'и': 1,
                     u'й': 5,
                     u'к': 2,
                     u'л': 2,
                     u'м': 2,
                     u'н': 1,
                     u'о': 1,
                     u'п': 2,
                     u'р': 2,
                     u'с': 2,
                     u'т': 2,
                     u'у': 3,
                     u'ф': 8,
                     u'х': 5,
                     u'ц': 8,
                     u'ч': 5,
                     u'ш': 8,
                     u'щ': 8,
                     u'ъ': 15,
                     u'ы': 5,
                     u'ь': 5,
                     u'э': 10,
                     u'ю': 8,
                     u'я': 3,
                     u'*': 0}

letters_in_the_bag = {u'а': 10,
                      u'б': 3,
                      u'в': 5,
                      u'г': 3,
                      u'д': 5,
                      u'е': 10,
                      u'ё': 10,
                      u'ж': 1,
                      u'з': 2,
                      u'и': 9,
                      u'й': 2,
                      u'к': 6,
                      u'л': 5,
                      u'м': 4,
                      u'н': 8,
                      u'о': 10,
                      u'п': 5,
                      u'р': 6,
                      u'с': 6,
                      u'т': 6,
                      u'у': 3,
                      u'ф': 1,
                      u'х': 1,
                      u'ц': 1,
                      u'ч': 2,
                      u'ш': 1,
                      u'щ': 1,
                      u'ъ': 1,
                      u'ы': 2,
                      u'ь': 2,
                      u'э': 1,
                      u'ю': 1,
                      u'я': 2,
                      u'*': 4}


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
    with codecs.open("15_letter_words_sushestvitelnie", encoding='utf-8', mode="r") as f:
        words = set(f.read().split("\n"))
    return words


def word_value(word):
    word_length = len(multiplicators["letter_multiplicator"])

    letter_values = [letters_value_map[c] for c in word]

    multi = multiplicators["letter_multiplicator"]
    letter_values_multiplied = [0] * word_length
    for i in range(len(letter_values)):
        letter_values_multiplied[i] = letter_values[i] * multi[i]

    word_full_value = sum(letter_values_multiplied) * multiplicators["word_multiplicator"]

    return word_full_value


def bag_has_sufficient_letters_for_word(word):
    counter = Counter(word)
    for c in counter:
        if counter[c] > letters_in_the_bag[c]:
            return False
    return True


main()
