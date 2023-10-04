from src.get_frequencies.get_frequencies import (get_frequencies)

def test_return_a_dictionary_that_represents_frequencies_of_each_character_in_the_string():
    """Should ignore spaces"""
    expected = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
    result = get_frequencies('hello world')
    print(f'Result is: {result}')
    assert result == expected
