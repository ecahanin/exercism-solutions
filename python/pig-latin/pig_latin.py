"""functions to translate english into pig latin"""

def translate(text):
    """translates a word or phrase into pig latin"""
    return ' '.join([translate_word(word) for word in text.split()])
    
def translate_word(text):
    """translates a single word into pig latin"""
    vowels = ['a', 'e', 'i', 'o', 'u']

    if text[0] in 'xy' and text[1] not in vowels + ['y']:
        return text + 'ay'
    for i, letter in enumerate(text):
        if i > 0:
            vowels.append('y')
        if letter == 'q' and text[i+1] == 'u':
            return text[i+2:] + text[:i+2] + 'ay'
        if letter in vowels:
            return text[i:] + text[:i] + 'ay'
