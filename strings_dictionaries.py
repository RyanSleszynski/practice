import os


def preprocessing(text: str, wanted_characters: str):
    """
    Removes all unwanted characters and excess spaces

    :param text a string that needs to be processed
    :param wanted_characters a string of characters that you do NOT want removed
    :return: str
    """
    has_spaces = False
    # replaces unwanted characters and with a space
    for character in text:
        if character not in wanted_characters:
            text = text.replace(character, ' ')
        elif character == ' ':
            has_spaces = True
    # This loop removes all consecutive spaces
    if has_spaces:
        while True:
            max_spaces = 0
            current_max_spaces = 0
            for character_index in range(len(text) - 1):
                if text[character_index] != ' ' and text[character_index + 1] == ' ':
                    current_max_spaces = 1
                elif text[character_index] == ' ' and text[character_index + 1] == ' ':
                    current_max_spaces += 1
                else:
                    if current_max_spaces > max_spaces:
                        max_spaces = current_max_spaces
                    else:
                        current_max_spaces = 0
            if max_spaces % 2 == 0:
                text = text.replace('  ', ' ')
            elif max_spaces % 2 != 0 and max_spaces != 1:
                text = text.replace('   ', ' ')
            else:
                break
    return text


def get_stopwords_list(stop_word_file):
    with open(os.path.join(os.getcwd(), stop_word_file), 'r', encoding='utf8') as stop_word_file:
        stop_word_file = stop_word_file.read()
        stop_word_list = stop_word_file.split()
    return stop_word_list


def auto_correct_word(word):  # already implemented, you need not do anything

    from autocorrect import Speller
    spell = Speller(lang='en')
    return spell(word)


def get_letter_frequency(cleaned_content):

    letter_freq_dict = dict()

    # we remove spaces in the content but do not need to make a deep copy because
    # strings are immutable
    cleaned_content = cleaned_content.replace(' ', '')

    for character in cleaned_content:
        if character in letter_freq_dict:
            letter_freq_dict[character] += 1
        else:
            letter_freq_dict[character] = 1

    return letter_freq_dict


def get_word_frequency(cleaned_content):

    word_freq_dict = dict()

    cleaned_content_words = cleaned_content.split()

    for word in cleaned_content_words:
        if word not in word_freq_dict:
            word_freq_dict[word] = 1
        else:
            word_freq_dict[word] += 1

    return word_freq_dict


def get_list_of_unique_words(cleaned_content):

    unique_word_list = []

    # this separates the words in cleaned content into a list of words to be iterated over
    cleaned_content_words = cleaned_content.split()

    # this creates a list of all the unique words with no repeats
    unique_word_list = [word for word in cleaned_content_words if word not in unique_word_list]

    return unique_word_list


def get_useful_words(cleaned_content, stop_word_list):
    # this separates the words in cleaned content into a list to be iterated over
    cleaned_content_words = cleaned_content.split()
    # this creates a list of all the words that are not in stop words
    useful_word_list = [word for word in cleaned_content_words if word not in stop_word_list]

    return useful_word_list


def get_keywords(useful_word_list: list, num_of_top_words: int):
    """
    Returns a list of the most frequent words passed into useful_word_list parameter

    :param useful_word_list: a list of words to consider for keywords
    :param num_of_top_words: the number of top words wanted
    :return: a list of
    """
    # returns a list of UP TO 6 most frequent out of useful_word_list
    # if there is a tie return all the words tied.
    # for example: word1:6, word2:6, word3: 5, word4: 5, word5: 4, word6: 4, word7: 4, word8:4
    # all words from word1 to word8 shall be returned as the output in a list
    # print the useful_word_list in order of their frequency, the most frequent words come first
    possible_keywords_count = {}
    possible_keywords = []

    # in this loop we are counting the words that are in the useful_word_list
    # and adding them to a dictionary if they do not exist in it already
    # if they already exist then the count is increased by 1
    for word in useful_word_list:
        if word not in possible_keywords_count:
            possible_keywords_count[word] = 1
        else:
            possible_keywords_count[word] += 1

    # This loop goes through the dictionary to find the count of the word that is most frequent
    # this will be used in the following loop as a point to start from
    max_frequency = 0
    for word in possible_keywords_count:
        if possible_keywords_count[word] > max_frequency:
            max_frequency = possible_keywords_count[word]

    # This loop will run while there are at least num_of_top_words in the possible_keywords
    # here old represents the current count we are comparing all counts to.
    old = max_frequency
    while len(possible_keywords) < num_of_top_words:  # need another condition here
        new = 0

        for word in possible_keywords_count:
            # if the word currently under consideration has the same count as the current max frequency
            # then add that word to the list
            if word not in possible_keywords and possible_keywords_count[word] == old:
                possible_keywords.append((word, possible_keywords_count[word]))

            # if the count of the word currently under consideration is less than the current old
            # and greater than the new at this point then that is the next frequency we check for
            # once the outer loop runs again
            elif new < possible_keywords_count[word] < old:
                new = possible_keywords_count[word]
        old = new

    return possible_keywords


# How to invert dictionary i.e. from values to keys
def get_inverted_dict(d):
    inverse = dict()
    # this invert will work only if you have only one value mapped to a key In the case of dictionary of frequency of
    # word or letter, there would be one-on-one mapping between keys and values We will have only one frequency for
    # each word or each letter
    for key in d:
        inverse[d[key]] = key
    return inverse


# How to invert dictionary i.e. from values to keys
def invert_dict_multivalues(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


def is_palindrome_iterative(text):

    if text == None:
        raise ValueError("is_palindrome_iterative function parameter must have at least one letter in a string.")
    elif not(isinstance(text, str)):
        raise TypeError("TypeError: is_palindrome_iterative: Argument \"text\" must be a string.")
    else:
        text_list = list(text)
        index = 0
        decrement = 1
        while text_list[index] == text_list[len(text_list) - decrement]:
            if index == len(text_list) // 2:
                return True
            index += 1
            decrement += 1

        return False


if __name__ == "__main__":
    pass
