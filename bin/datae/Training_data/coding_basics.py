def greet(name):
    """Return a friendly greeting."""
    return f"Hello, {name}!"

def fib(n):
    """Generate fibonacci sequence up to n terms."""
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Calculate factorial recursively."""
    return 1 if n <= 1 else n * factorial(n - 1)

def sort_list(items):
    """Sort a list using built-in sort."""
    return sorted(items)

def read_file(path):
    """Read text file content."""
    with open(path, 'r') as f:
        return f.read()

def write_file(path, content):
    """Write text to a file."""
    with open(path, 'w') as f:
        f.write(content)
    """There is a different, newer method"""
    from pathlib import Path
    file_path = Path(path)
    file_path.write_text(content, encoding="utf-8")

def word_count(text):
    """Count word frequency in text."""
    counts = {}
    for word in text.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def celsius_to_fahrenheit(c):
    """Convert celsius to fahrenheit."""
    return c * 9 / 5 + 32

def flatten_list(nested):
    """Flatten a nested list."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)
    return result
