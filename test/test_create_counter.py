from src.create_counter.create_counter import (create_counter)

def test_should_accept_a_number_as_its_only_argument_and_returns_dic_with_2_funcs_to_change_and_return_counter_value():
    # """Should ignore spaces"""
    # arrange
    counter = create_counter(10)
    up = counter['up']
    down = counter['down']
    expected = 11
    result = up()
    print(f'Result is: {result}')
    assert result == expected

    expected = 12
    result = up()
    print(f'Result is: {result}')
    assert result == expected

    expected = 11
    result = down()
    print(f'Result is: {result}')
    assert result == expected

    expected = 10
    result = down()
    print(f'Result is: {result}')
    assert result == expected