# palindrome_checker.py
def is_palindrome(string):
    """
    Checks if a given string is a palindrome.
    A palindrome reads the same backward as forward.
    """
    string = string.lower().replace(" ", "")  # Normalize by removing spaces and converting to lowercase
    return string == string[::-1]

if __name__ == "__main__":
    print("Palindrome Checker")
    test_words = ["radar", "hello", "level", "world", "madam"]
    for word in test_words:
        result = "is" if is_palindrome(word) else "is not"
        print(f"'{word}' {result} a palindrome")
