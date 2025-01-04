# fizzbuzz.py
def fizz_buzz(n):
    """
    Returns "Fizz" if the number is divisible by 3,
    "Buzz" if it's divisible by 5,
    "FizzBuzz" if divisible by both, 
    or the number itself if none of these conditions are met.
    """
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return n

if __name__ == "__main__":
    print("FizzBuzz Example")
    for i in range(1, 21):
        print(fizz_buzz(i))
