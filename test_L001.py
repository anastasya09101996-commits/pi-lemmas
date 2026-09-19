# tests/test_L001.py
import itertools

def even_palindromes(max_half=3):
    for half in range(1, max_half + 1):
        for first in range(1, 10):
            for rest in itertools.product(range(10), repeat=half - 1):
                h = [first] + list(rest)
                yield int("".join(map(str, h + h[::-1])))

def test_even_palindromes_divisible_by_11():
    for n in even_palindromes():
        assert n % 11 == 0, n

def test_known_example():
    assert 228822 == 11 * 20802

def test_odd_length_not_covered():
    assert 12321 % 11 != 0

if __name__ == "__main__":
    test_even_palindromes_divisible_by_11()
    test_known_example()
    test_odd_length_not_covered()
    print("L-001: all tests green")