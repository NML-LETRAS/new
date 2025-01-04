import re  # For removing non-alphanumeric characters

def is_palindrome(string):
    """
    Checks if a given string is a palindrome.
    A palindrome reads the same backward as forward.
    """
    # Normalize by removing non-alphanumeric characters, converting to lowercase, and trimming spaces
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', string.lower())
    return clean_string == clean_string[::-1]

def check_multiple_palindromes(words):
    """
    Checks multiple strings and prints whether each is a palindrome.
    """
    print("\nPalindrome Results:")
    for word in words:
        result = "is" if is_palindrome(word) else "is not"
        print(f"'{word}' {result} a palindrome.")

if __name__ == "__main__":
    print("Palindrome Checker")

    # Check predefined test cases
    test_words = ["radar", "hello", "level", "world", "A man, a plan, a canal: Panama", "No lemon, no melon"]
    check_multiple_palindromes(test_words)

    # Allow user to input their own strings
    while True:
        user_input = input("\nEnter a string to check for palindrome (or type 'exit' to quit): ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        result = "is" if is_palindrome(user_input) else "is not"
        print(f"'{user_input}' {result} a palindrome.")
