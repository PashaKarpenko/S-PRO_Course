# 2) Реализуйте модуль  word_utils.py, позволяющий:
import re

# - очистить предложение от знаков препинания;
def punctuation_removal(str):
    return re.sub(r'[^a-z A-Z а-я А-Я 0-9]', " ", str)

# - получить список слов из предложения;
def get_list_of_words(str):
    return str.split()

# - получить самое длинное слово в предложении;
def longest_word_in_sentence(lst):
   return max(lst, key=len)
