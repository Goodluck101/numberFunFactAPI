import math

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_armstrong(n: int) -> bool:
    """Check if a number is an Armstrong number (Narcissistic number)."""
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def is_perfect(n: int) -> bool:
    """Check if a number is a perfect number."""
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def digit_sum(n: int) -> int:
    """Calculate the sum of the digits of a number."""
    return sum(int(digit) for digit in str(n))

def classify_number(n: int) -> dict:
    """Classify the number based on mathematical properties."""
    properties = []
    
    if is_armstrong(n):
        properties.append("armstrong")
    
    properties.append("even" if n % 2 == 0 else "odd")

    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": digit_sum(n)
    }
