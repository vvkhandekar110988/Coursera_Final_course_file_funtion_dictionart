punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']


def strip_punctuation(str1):
    for ch in punctuation_chars:
        str1 = str1.replace(ch, '')
    return str1


def get_neg(str1):
    str1_lower = str1.lower()
    str1_lower_strip = strip_punctuation(str1_lower)
    str1_lower_strip_list = str1_lower_strip.split()
    count = 0
    for word in str1_lower_strip_list:
        for negative_word in negative_words:
            if word == negative_word:
                count += 1
    return count


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
'''
for i in negative_words:
    print(i)
'''