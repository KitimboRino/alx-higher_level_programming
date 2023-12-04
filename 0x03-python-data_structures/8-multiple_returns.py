#!/usr/bin/python3
def multiple_returns(sentence):
    # Check if the sentence is empty and set it to None
    if not sentence:
        sentence = None

    # Calculate the length of the sentence
    sen_len = len(sentence) if sentence else 0

    # Return a tuple with the length and the first character of the sentence
    return (sen_len, sentence[:1] if sentence else None)
