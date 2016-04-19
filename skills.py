"""Skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::

        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different::

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    output = []
    seen = set()
    for word in words:
        #if value has not been encountered yet,
        #add it to both list and set.
        if word not in seen:
            output.append(word)
            seen.add(word)

    return output

#passed


def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2] PASSED
    """
    #I'm missing the code for the duplicates
    #

    #start with empty list
    lists = []

    #for loop. Checking items1 list first for doubles.
    for i in items1:
    # checking items2 for doubles
        if i in items2:
    #if found doubles add them together
            lists.append(i)

    # am I missing 'sorted' here? return sorted(lists)  ?
    return lists


def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #split the words
    words = phrase.split(" ")
    # empty dictionary. will count the words
    counts = {}

    for word in words:
        if word in counts:
            #if the word is already in the dictionary add it
            counts[word] += 1
            #setting the value to 1
        else:
            counts[word] = 1

    return counts


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    boy         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    #split the words
    words = phrase.split(" ")

    # I think that there is an error here. When putting my answer in the terminal
    # it told me that the key 'man' is not translated to the value 'matey'. That's because
    # in the text it actually says that the key is 'sir'. So I changed the key to 'man'.
    pirate_dict = {"man": "matey", "hotel": "fleabag inn",
            "student": "swabbie",
            "boy": "matey",
            "professor": "foul blaggart",
            "restaurant":  "galley",
            "your": "yer",
            "excuse": "arr",
            "students": "swabbies",
            "are": "be",
            "restroom": "head",
            "my": "me",
            "is":   "be"}

    translation = []

    for word in words:
        if word in pirate_dict:
            pirate_translation = pirate_dict[word]
            translation.append(pirate_translation)
        else:
            translation.append(word)

    return " ".join(translation)


def sort_by_word_length(words):
    """Given list of words, return list of ascending (len, [words]).

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- the length
    of the words for that word-length, and the list of words of
    that word length.

    For example::

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]
    """
    #creating an empty dictionary
    length_words_dict = {}

    for word in words:
        #gets the length of the word
        length_word = len(word)
        # if word length is already in the dictionary, add it
        if length_word in length_words_dict:
            length_words_dict[length_word].append(word)
        else:
            #first time for each word length it needs to get a new list
            new_list = [word]
            #adding the keys to the dictionary
            length_words_dict[length_word] = new_list

    return length_words_dict.items()


def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """

    # creating an empty list of numbers
    numbers_list = []

    for number in numbers:
        if number in numbers_list:
            #adds up to 0 then append
            add_numbers[number_list].append(number)
        else:
            #otherwise don't
            pass

    return numbers_list


def kids_game(part_of_chain, return_list, names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # should probably use dictionaries because the key in the dictionary
    # is the first word in the pair. The list will contain al the second words
    # the stuff below is some craziness..my brain is fried ;)

    last_word = part_of_chain[-1]

    if last_word not in names:
        return

    next_word = names[last_word]

    for next_word in next_words:
        if next_word in part_of_chain:
            continue

        new_chain = copy.copy(part_of_chain)
        new_chain.append(next_word)

        #count how many words
        if len(new_chain) < length_of_chain:
            append_words(new_chain, part_of_chain, return_list)
        else:
            return_list.append(new_chain)  
    return last_word


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
