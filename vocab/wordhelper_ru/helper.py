import re

r = re.compile("(?<=app__words_word\">).*?(?=<span class=\"app__words_word_rate)")
filename = "vocab/wordhelper_ru/wordhelper_ru_15_letter_words_2"
with open(filename + ".html", "r+") as f:
    with open(filename + "_list.txt", "w+") as res:
        for line in f.readlines():
            lst = r.findall(line)
            for word in lst:
                word = word.strip()
                is_prilagatelnoe = word.endswith("ый") or word.endswith("ий")
                is_glagol = word.endswith("ться")
                if " " not in word and len(word) >= 15 and not is_prilagatelnoe and not is_glagol:
                    res.write(word+"\n")

