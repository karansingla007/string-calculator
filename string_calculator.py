# string_calculator.py
import re


def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ","
    custom_delimiter_pattern = r"^//(.+)\n(.*)"

    if numbers.startswith("//"):
        match = re.match(custom_delimiter_pattern, numbers, re.DOTALL)
        if match:
            delimiter, numbers = match.groups()

    # support newlines as delimiter
    numbers = numbers.replace("\n", delimiter)

    split_numbers = numbers.split(delimiter)

    parsed_numbers = []
    negative_numbers = []

    for num in split_numbers:
        if num.strip():
            n = int(num)
            if n < 0:
                negative_numbers.append(n)
            parsed_numbers.append(n)

    if negative_numbers:
        raise ValueError(f"negative numbers are not allowed: {', '.join(map(str, negative_numbers))}")

    return sum(parsed_numbers)

print(add("1"))
print(add("1,2"))
print(add("1,2,3,4,5"))
print(add("1\n2,3"))
print(add("//;\n1;2"))
print(add("//|\n1|2|3"))
print(add("1,-2"))