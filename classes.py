from collections import Counter

class Multiplicator:

    def __init__(self, word, letters):
        self.word = word
        self.letters = letters


class Word:
    value = None

    def __init__(self, word):
        self.word = word

    def __repr__(self):
        return f'Word({self.word}: {self.value})'


class WordFile:
    def __init__(self, path, encoding=None):
        self.path = path
        self.encoding = encoding


class VocabAnalysis:
    letter_count = Counter()

    def __repr__(self):
        return f'VocabAnalysis(\nfrequency_of_letters: {self.letter_count.most_common()}\n)'
