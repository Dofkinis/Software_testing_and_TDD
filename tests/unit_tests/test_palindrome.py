def is_palindrome(word):
    return str(word)[::1].lower() == str(word).lower()


def test_is_palindrome():
    assert is_palindrome("aha")


def test_is_palindrome_with_caps():
    assert is_palindrome("Aha")


def test_is_palindrome_when_number():
    assert is_palindrome(121)