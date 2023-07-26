from src.herd_the_babies.herd_the_babies import herd_the_babies

def test_returns_a_single_word_in_upper_if_true():
    expected = 'Aa'
    result = herd_the_babies('aA')

    assert result == expected

def test_returns_a_many_word_():
    expected = 'AaBbbCcc'
    result = herd_the_babies('aAbbBcCc')

    assert result == expected