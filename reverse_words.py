# goal: invert letters a->z b->y etc. "wizard" spells "draziw", wizard backwards
# how many words are like this in the any language?
#
# author: Robert Sebescen (pgrobban at gmail dot com)


def get_words_from_file(file):
    """ Reads a word list (one word per line) and returns the words as a list. """
    return [line.strip() for line in open(file)]

def invert_and_reverse_word(word, alphabet="abcdefghijklmnopqrstuvwxyz", transform_dict=None):
    """ Inverts a word such that each letter in the word is replaced by its
     corresponding letter from the end of the alphabet, e.g. in the English
     alphabet a -> z, b -> y, c -> x and so on.
     Then, reverse the resulting word.
     The function assumes that cases doesn't matter, so the returned word is
     in lowercase.
     
     The second argument for the function is a string containing the letters of the alphabet
     which must be in correct order.
     The function assumes that all letters in the given word are in the given
     alphabet. If there are additional letters that might appear in the word but should
     be counted as different letters, e.g. if "ü" should be considered as a "u",
     create a dictionary with the desired transformations and pass it as the third
     argument to this function."""
   
    word = word.lower()
    inv_letters = []
    for letter in word:
        if letter in alphabet:
            inv_letter = alphabet[-alphabet.index(letter)-1]
        else:
            try:
                inv_letter = transform_dict[letter]
                if inv_letter is None:
                    continue;
            except KeyError:
                raise ValueError("Didn't recognize the letter " + letter)

        inv_letters.append(inv_letter)
    inv_letters.reverse()
    return "".join(inv_letters)

def invert_and_reverse_words(words, 
    alphabet="abcdefghijklmnopqrstuvwxyz", 
    transform_dict=None, 
    only_equals=False):
    """ Given a list of words, this finds and returns a 2-tuple of all words
     of the format (word, inverse of word). 
    
     You can specify which alphabet to use as the second argument, which must
     ba string in the correct order. By default, this uses the English letters a-z.
     The function assumes that words in the list will consist of letters that
     are in the given alphabet. If there are additional letters that might appear 
     in the words but should
     be considered as different letters, e.g. if "ü" should be considered as a "u",
     create a dictionary with the desired transformations and pass it as the third
     argument to this function. 
     
     If the fourth argument is set to True, the returned list will not contain
     tuples; instead it's an ordinary list whose elements are words that have
     the property of being equal to their inverse reverse.
     """

    inverted_words = []
    for word in words:
        inverted_word = invert_and_reverse_word(word, alphabet, transform_dict)
        if not only_equals:
            inverted_words.append((word, inverted_word))
        elif only_equals and word == inverted_word:
            inverted_words.append(word)
        
    return inverted_words


# uncomment the following lines for example usage

#words = get_words_from_file("words.txt")
#print(invert_and_reverse_words(words, only_equals=False))
#
#alphabet = "abcdefghijklmnopqrstuvwxyzåäö"
#transform_dict = {
#    "-" : None,
#    "." : None,
#    "'" : None,
#    "é" : "e",
#    "è" : "e",
#    "ë" : "e",
#    "ü" : "u",
#    "ø" : "ö",
#    "ß" : "s",
#    "ç" : "c",
#    "æ" : "ä",
#    "á" : "a",
#    "ã" : "a",
#    "à" : "a",
#    "ô" : "o",
#    "ò" : "o",
#    "õ" : "o",
#    "ó" : "o",
#    "í" : "i",
#    "ï" : "i",
#    "î" : "i",
#    "ÿ" : "y",
#    "ñ" : "n",
#}
#  
#words = get_words_from_file("ss100.txt")
#print(invert_and_reverse_words(words, alphabet, transform_dict, True))
    
