from src.lengthen_date.lengthen_date import (lengthen_date)

def xtest_should_take_a_date_in_the_format_21032017_and_return_a_string_in_the_format_Tuesday_21st_March_2017():
    # arrange
    result = lengthen_date('21.03.2017')
    expected = 'Tuesday 21st March 2017'
    print(f'Result is: {result}')
    assert result == expected