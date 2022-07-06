def print_upper_words (words, must_start_with):
    """Given list of words, return the capitalized version.

    For example:
      print_upper_words(["hello","hey","yo","goodbye","yes"])

    Should return (not print):
      10
    """  
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
