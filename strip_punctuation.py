''' To start, define a function called strip_punctuation which takes one parameter, a string which represents a word,
and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for
strings.) '''


def strip_punctuation(str1):
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    for ch in punctuation_chars:
        str1 = str1.replace(ch, '')
    return str1


a = strip_punctuation('#Amazing')
print(a)
