
import json
import libs.greek_lib as greeklib

# Exercise 1
file1 = open('words_to_order/set_words_1.json', encoding="utf8")   
words1 = json.load(file1)
#greeklib.order_words(words1)

# Exercise 2
file2 = open('words_to_order/set_words_2.json', encoding="utf8")   
words2 = json.load(file2)
#greeklib.order_words(words2)

# Exercise 3
file3 = open('words_to_order/set_words_3.json', encoding="utf8")   
words3 = json.load(file3)
#greeklib.order_words(words3)

# Ejercicio 4
file4 = open('words_to_order/set_words_4.json', encoding="utf8")   
words4 = json.load(file4)
greeklib.order_words(words1)

