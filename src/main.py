from constants import ABOVE_100, TENS, UNDER_20


def number_to_words(num: int) -> str:
    """Converts a non-negative integer into its English word representation.

    :param num: The integer to convert.
    :raises ValueError: If the input number is negative.
    :returns: The English word representation of the number.
    """
    if num < 0:
        raise ValueError("Number must be non-negative.")

    if num < 20:
        return UNDER_20[num]

    if num < 100:
        quotient, remainder = divmod(num, 10)
        if remainder == 0:
            return TENS[quotient]
        return f"{TENS[quotient]} {UNDER_20[remainder]}"

    # Find the largest magnitude key in ABOVE_100 that fits into num
    pivot = max(key for key in ABOVE_100 if key <= num)
    quotient, remainder = divmod(num, pivot)

    base_string = f"{number_to_words(quotient)} {ABOVE_100[pivot]}"
    
    if remainder != 0:
        return f"{base_string} {number_to_words(remainder)}"
    
    return base_string


def main() -> None:
    """Main entry point of the script for user interaction."""
    user_input = input("Enter a non-negative integer: ")
    try:
        num = int(user_input.strip())
        word_representation = number_to_words(num)
        print(word_representation)
    except ValueError as e:
        # Catches both non-integer inputs and negative numbers 
        # (if the latter is raised by number_to_words)
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
