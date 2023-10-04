from src.sentence_to_camel_case.sentence_to_camel_case import (sentence_to_camel_case)


def test_returns_a_single_word_in_upper_if_true():
    expected = 'This'
    result = sentence_to_camel_case('this', True)
    print(f'Result is: {result}')
    assert result == expected

    expected = 'ThisSentence'
    result = sentence_to_camel_case('this sentence', True)
    print(f'Result is: {result}')
    assert result == expected

    expected = 'thisSentence'
    result = sentence_to_camel_case('this sentence', False)
    print(f'Result is: {result}')
    assert result == expected

    expected = 'ThisBiggerStrangeSentence'
    result = sentence_to_camel_case('This Bigger strange Sentence', True)
    print(f'Result is: {result}')
    assert result == expected

expected = 'WhyAreYouYelling'
result = sentence_to_camel_case('WHY ARE YOU YELLING',  True)
assert result == expected

expected = 'ThisIsABitOdd'
result = sentence_to_camel_case('tHiS iS a BiT oDd',  True)
assert result == expected

expected = 'These1Include2Numbers3'
result = sentence_to_camel_case('these 1 include 2 numbers 3', True)
assert result == expected
