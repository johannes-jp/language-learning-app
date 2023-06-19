from libvoikko import Voikko


def analyze_finnish_word(word):
    v = Voikko("fi")
    analysis = v.analyze(word)

    return analysis


word = "koira"
analysis = analyze_finnish_word(word)
for a in analysis:
    print(a)
