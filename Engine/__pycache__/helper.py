import re

def remove_words(input_string, words_to_remove):
    #split the input string into words
    words = input_string.split()

    #remove the specified words
    filtered_words = [word for word in words if word.lower not in words_to_remove]

    #join the filtered words back into a string
    result_string = ' '.join(filtered_words)
    
    return result_string