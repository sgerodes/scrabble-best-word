#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import Counter

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

words_created = [u'иней', u'но', u'кпун', u'длиа', u'кст', u'а', u'т', u'каш', u'н', u'о', u'н', u'вера', u'д', u'и',
                 u'ейс', u'офет', u'ю', u'ыл', u'ербо', u'о', u'эбн', u'щипц', u'че',
                 u'хам', u'уня', u'под', u'гмус', u'сть', u'рча', u'', u'', u'', u'',
                 u'*опиь', u'я', u'ив', u'авоети*а', u'', u'', u'', u'']

counter = Counter(u'')

for word in words_created:
    for c in word:
        letters_in_the_bag[c] -= 1

for letter in letters_in_the_bag:
    number = (str(letters_in_the_bag[letter]) if letters_in_the_bag[letter] > 0 else '--')
    if letter in counter:
        if number == str(counter[letter]):
            number += ' (' + str(counter[letter]) + ') !!!!!'
        else:
            number += ' (' + str(counter[letter]) + ')'
    word = letter.encode("utf8") + " " + number
    print word
