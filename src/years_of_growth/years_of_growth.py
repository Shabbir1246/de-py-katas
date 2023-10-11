
def years_of_growth(
    initial_population,
    target_population,
    growth_rate,
    net_migration):

    years_req = 0
    current_population = initial_population
    growth_multiplier = growth_rate / 100
    while current_population < target_population:
        current_population += current_population * growth_multiplier + net_migration
        years_req += 1
        # print (current_population, years_req)

    return years_req