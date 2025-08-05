import re
import pytest

def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiters = [',', '\n']

    # Check for custom delimiter(s)
    if numbers.startswith('//'):
        header, numbers = numbers.split('\n', 1)
        custom_delimiters = re.findall(r'\[(.*?)\]', header)
        if custom_delimiters:
            delimiters.extend(custom_delimiters)
        else:
            delimiters.append(header[2:])

    # Create a regex pattern for all delimiters
    delimiter_pattern = '|'.join(map(re.escape, delimiters))
    tokens = re.split(delimiter_pattern, numbers)

    negatives = []
    total = 0

    for token in tokens:
        if not token:
            continue
        num = int(token)
        if num < 0:
            negatives.append(num)
        elif num <= 1000:
            total += num

    if negatives:
        raise ValueError(f"negative numbers are not allowed: {', '.join(map(str, negatives))}")

    return total