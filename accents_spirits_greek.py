import re
from termcolor import colored
from scikirt import t

def print_text(text, items):
    colors = {'badass_spirit_patron':'red',
            'soft_spirit_pattern':'green',
            'acute_accent_pattern':'blue',
            'grave_accent_pattern':'magenta',
            'circumflex_pattern': 'cyan'}
    print("----------------------------------------------")
    print("* * *          Highlighted Text          * * *")
    print("----------------------------------------------")
    highlighted_text = text
    for key in items.keys():
        for word in items[key]:
            highlighted_text = highlighted_text.replace(word, colored(word, colors[key]))

    return highlighted_text

def print_text_separated(text, words, type):
    colors = {'badass_spirit_patron':'red',
            'soft_spirit_pattern':'green',
            'acute_accent_pattern':'blue',
            'grave_accent_pattern':'magenta',
            'circumflex_pattern': 'cyan'}
    print("----------------------------------------------")
    print("Greek Figure: "+colored(type, colors[type]))
    print("----------------------------------------------")
    highlighted_text = text
    for word in words:
        highlighted_text = highlighted_text.replace(word, colored(word, colors[type]))

    return highlighted_text

def find_features(text):

    badass_spirit_patron = r'[ἕὃὗ]+'
    soft_spirit_pattern = r'[ἀἐὐἘὖἦ]+'
    acute_accent_pattern = r'[άέήίόύώ]+'
    grave_accent_pattern =  r'[ὰὲὴὶὸὨὺ]+'
    circumflex_pattern = r'[ᾶῖῶῦῆῇ]+'

    words_with_rough_spirit = re.findall(badass_spirit_patron, text)
    words_with_gentle_spirit = re.findall(soft_spirit_pattern, text)
    words_with_acute_accent = re.findall(acute_accent_pattern, text)
    words_with_grave_accent = re.findall(grave_accent_pattern, text)
    words_with_circumflex = re.findall(circumflex_pattern, text)

    items = {
            'badass_spirit_patron': words_with_rough_spirit,
             'soft_spirit_pattern': words_with_gentle_spirit,
             'acute_accent_pattern': words_with_acute_accent,
             'grave_accent_pattern': words_with_grave_accent,
             'circumflex_pattern': words_with_circumflex
             }

    print(print_text(text, items))

    print(print_text_separated(text, words_with_rough_spirit, 'badass_spirit_patron'))
    print(print_text_separated(text, words_with_gentle_spirit, 'soft_spirit_pattern'))
    print(print_text_separated(text, words_with_acute_accent, 'acute_accent_pattern'))
    print(print_text_separated(text, words_with_grave_accent, 'grave_accent_pattern'))
    print(print_text_separated(text, words_with_circumflex, 'circumflex_pattern'))


# Ejemplo de uso
texto = """
Juan 1:1-3 Ἐν ἀρχῇ ἦν ὁ λόγος,
καὶ ὁ λόγος ἦν πρὸς τὸν θεόν,
καὶ θεὸς ἦν ὁ λόγος (2) οὗτος
ἦν ἐν ἀρχῇ πρὸς τὸν θεόν (3)
πάντα δι’ αὐτοῦ ἐγένετο, καὶ
χωρὶς αὐτοῦ ἐγένετο οὐδὲ ἕν ὃ
γέγονεν
"""

highlighted_text = find_features(texto)
print(highlighted_text)