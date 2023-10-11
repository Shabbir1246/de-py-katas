from src.years_of_growth.years_of_growth import (years_of_growth)

def test_should_take_4_parameters_a_starting_population_an_end_population_a_percentage_of_growth_and_a_netMigration_figure():
    """ If the population grows by the given percentage each year, plus an additional number of net migrants, 
    the function should calculate how 
    many years it takes until the end population total is reached."""
    expected = 25
    result = years_of_growth(1000, 2000, 2, 12)
    print(f'Result is: {result}')
    assert result == expected

