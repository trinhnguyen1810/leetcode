def intToRoman(num):
    """
    Convert an integer to a Roman numeral.
    """
    digits = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    
    roman_digits = []

    for symbol, value in digits.items():
        # We don't want to continue looping if we're done.
        if num == 0:
            break
        count, num = divmod(num, value)
        # Append "count" copies of "symbol" to roman_digits.
        roman_digits.append(symbol * count)
    
    return "".join(roman_digits)

# Test the function
print(intToRoman(3749))  # Output: "MMMDCCXLIX"