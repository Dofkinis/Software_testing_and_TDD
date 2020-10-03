def capitalize_letters(word):
    return word.upper()


def test_capitalize_letters():
    assert capitalize_letters("word") == "WORD"