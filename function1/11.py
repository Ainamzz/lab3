def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
word = input("Enter word or sentence:")
print(is_palindrome(word))