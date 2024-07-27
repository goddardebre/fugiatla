def reverse_words_order(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

input_sentence = "Prints out the string with the words in reverse order."
reversed_sentence = reverse_words_order(input_sentence)
print(reversed_sentence)
