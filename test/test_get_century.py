from src.get_century.get_century import (get_century)

def test_should_take_a_year_as_a_number_and_return_the_century():
    """ should work up to and including the year 10,000 (the '101st' century) """
    expected = 'Too far in future'
    result = get_century(11000)
    print(f'Result is: {result}')
    assert result == expected

    expected = '11th'
    result = get_century(1099)
    print(f'Result is: {result}')
    assert result == expected
    assert get_century(99) == '1st'
    assert get_century(101) == '2nd'
    assert get_century(210) == '3rd'
    assert get_century(301) == '4th'
    assert get_century(401) == '5th'
    assert get_century(901) == '10th'
    assert get_century(1099) == '11th'
    assert get_century(1199) == '12th'
    assert get_century(1299) == '13th'
    assert get_century(1301) == '14th'
    assert get_century(1877) == '19th'
    assert get_century(1999) == '20th'
    assert get_century(2001) == '21st'
    assert get_century(2101) == '22nd'
    assert get_century(2201) == '23rd'
    assert get_century(2301) == '24th'

