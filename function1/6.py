def reverse_sentence():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    words.reverse()
    print(" ".join(words))

reverse_sentence()
