from src.get_distinct_letters.get_distinct_letters import (get_distinct_letters)


def test_returns_a_sorted_string_of_all_letters_unique_to_two_given_strings():
    expected = 'dehrw'
    result = get_distinct_letters('hello', 'world')
    print(f'Result is: {result}')
    assert result == expected

    expected = 'Odehorw'
    result = get_distinct_letters('hello', 'wOrld')
    print(f'Result is: {result}')
    assert result == expected

    expected = ' 1Odehorw'
    result = get_distinct_letters('hello 1', 'wOrld')
    print(f'Result is: {result}')
    assert result == expected